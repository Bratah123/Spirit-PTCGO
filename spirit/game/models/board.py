import uuid
import json
import random
import logging
from typing import Dict, Any, List, Optional, Union
from spirit.game.attributes import AttrID, CardType, PokemonStage, Rarities, PlayerAttrID
from spirit.game.models.card import Card
from spirit.game.scripts.cards import loader as card_loader
from spirit.network.message_names import OutboundMsg

# Number of bench slots (standard rules). Serialized onto the bench PlayArea
# as AttrID.AREA_SLOTS so the client's BenchLayout can space cards.
BENCH_SLOT_COUNT = 5


class BoardEntity:
    """Base class representing any physical or structural entity on the client's playmat."""
    def __init__(
        self,
        entity_id: Optional[str] = None,
        parent_id: Optional[str] = None,
        owning_player_id: Optional[str] = None,
        archetype_id: Optional[str] = None
    ):
        self.entity_id: str = entity_id or str(uuid.uuid4())
        self.parent_id: Optional[str] = parent_id
        self.parent: Optional['BoardEntity'] = None
        self.owning_player_id: Optional[str] = owning_player_id
        self.archetype_id: Optional[str] = archetype_id
        # Mirror of the client's A.m slot stamp: the positionInParent of the
        # last EntityMoved sent for this entity. BenchLayout renders each card
        # at this slot and never renumbers when a neighbor leaves the bench.
        self.board_slot: Optional[int] = None
        self.attributes: Dict[int, Any] = {}
        # Per-attribute base values: serialized as originalValue when the live
        # value diverges (e.g. HP max vs remaining -- client damage = max - value).
        self.attribute_originals: Dict[int, Any] = {}
        self.children: List[BoardEntity] = []

    def set_attribute(self, key: Union[int, AttrID], value: Any):
        """Sets an attribute on this entity."""
        attr_key = key.value if isinstance(key, AttrID) else key
        self.attributes[attr_key] = value

    def get_attribute(self, key: Union[int, AttrID], default: Any = None) -> Any:
        """Retrieves an attribute value from this entity."""
        attr_key = key.value if isinstance(key, AttrID) else key
        return self.attributes.get(attr_key, default)

    def add_child(self, child: 'BoardEntity', position: Optional[int] = None):
        """Adds a child entity to this entity, establishing the parent-child relation.

        position inserts at a specific index (e.g. an evolution taking over its
        target's board slot); None appends to the end.
        """
        child.parent_id = self.entity_id
        child.parent = self
        if position is None or position >= len(self.children):
            self.children.append(child)
        else:
            self.children.insert(max(position, 0), child)

    def remove_child(self, child: 'BoardEntity'):
        """Removes a child entity from this entity."""
        if child in self.children:
            self.children.remove(child)
            child.parent_id = None
            child.parent = None

    def serialize_attributes(self) -> List[Dict[str, Any]]:
        """Formats the entity's attributes into the specific client-compatible JSON structure."""
        serialized = []
        for key, val in self.attributes.items():
            # If the attribute is NAME (10140) and it's a raw string, format it as localizable text.
            if key == AttrID.NAME.value and isinstance(val, str):
                formatted_val = {"id": val}
            else:
                formatted_val = val

            original_val = self.attribute_originals.get(key, formatted_val)
            serialized.append({
                "name": key,
                "value": formatted_val,
                "originalValue": original_val,
                "modValue": formatted_val
            })
        return serialized

    def is_hidden_from(self, viewer_id: Optional[str]) -> bool:
        """Whether this entity's identity should be hidden from the given viewer.

        Hidden entities serialize with attributes=null, which the client reads
        as "un-introduced" (SerializedEntity.Introduced == Attributes != null)
        and renders as a face-down card back in any zone. Structural entities
        (playmat, players, areas) are never hidden.
        """
        return False

    def serialize(self, viewer_id: Optional[str] = None) -> Dict[str, Any]:
        """Recursively serializes this entity and all its children to match the client expectation."""
        return {
            "entityID": self.entity_id,
            "parentID": self.parent_id,
            "owningPlayerID": self.owning_player_id,
            "entityName": self.get_entity_name(),
            "archetypeID": self.archetype_id,
            "attributes": None if self.is_hidden_from(viewer_id) else self.serialize_attributes(),
            "children": [child.serialize(viewer_id) for child in self.children]
        }

    def get_entity_name(self) -> str:
        """Returns the fully qualified class name for the client-side entity."""
        raise NotImplementedError("Subclasses must implement get_entity_name")


class PlayMat(BoardEntity):
    """Represents the root Playmat scene board entity (CakePlayMat)."""
    def __init__(self, entity_id: Optional[str] = None, theme_name: str = "playmat"):
        super().__init__(entity_id=entity_id)
        self.set_attribute(AttrID.NAME, theme_name)

    def get_entity_name(self) -> str:
        return "com.direwolfdigital.cake.rules.entities.CakePlayMat"


class PlayerEntity(BoardEntity):
    """Represents a player entity wrapper on the playmat (CakePlayerEntity)."""
    def __init__(self, owning_player_id: str, entity_id: Optional[str] = None):
        super().__init__(entity_id=entity_id, owning_player_id=owning_player_id)
        self.set_attribute(AttrID.NAME, "player")

    def get_entity_name(self) -> str:
        return "com.direwolfdigital.cake.rules.entities.CakePlayerEntity"


class PlayArea(BoardEntity):
    """Represents a play area (pile/zone) on the board (PlayArea)."""
    def __init__(self, area_name: str, owning_player_id: Optional[str] = None, entity_id: Optional[str] = None):
        super().__init__(entity_id=entity_id, owning_player_id=owning_player_id)
        self.set_attribute(AttrID.NAME, area_name)

    def get_entity_name(self) -> str:
        return "com.direwolfdigital.game.core.PlayArea"


def _match_render_attributes(card_obj: Card) -> Dict[int, Any]:
    """Full render-attribute map for an in-play card entity."""
    try:
        raw = card_obj.to_archetype_attributes(card_obj.key)
    except Exception as e:
        logging.warning(f"[BoardState] Could not build render attributes for {card_obj.guid}: {e}")
        return {}

    out: Dict[int, Any] = {}
    for aid_str, spec in raw.items():
        key = int(aid_str)
        vtype = spec.get("type")
        val = spec.get("value")
        # JSON-typed attributes (name, types, abilities) are carried as JSON
        # strings for the protobuf path; the SGS JSON path wants the parsed
        # structure so JsonFx maps it to the client's typed Attribute<T>.
        if vtype == "json" and isinstance(val, str):
            try:
                val = json.loads(val)
            except (ValueError, TypeError):
                pass
        out[key] = val

    out.pop(AttrID.EXPANSION.value, None)
    return out


class CardEntity(BoardEntity):
    """Base class for any card placed on the board (Pokemon, Energy, TrainerCard)."""
    def __init__(self, card_obj: Card, owning_player_id: Optional[str] = None, entity_id: Optional[str] = None):
        super().__init__(entity_id=entity_id, owning_player_id=owning_player_id, archetype_id=card_obj.guid)
        self.card_obj = card_obj
        # Carry the full render attribute set so the client's in-match card-face
        # renderer can build its image request (set code + collector number).
        self.attributes.update(_match_render_attributes(card_obj))
        # The mulligan-reveal carousel resolves each revealed card's archetype
        # through entity attribute 10000 (GetAttribute<ArchetypeID> in
        # MulliganCarouselRenderRequester.MulliganSetContents); a card without
        # it crashes the panel with ArgumentNullException on the lookup.
        self.set_attribute(AttrID.ARCHETYPE_ID, card_obj.guid)
        self._initialize_attributes()

    def _initialize_attributes(self):
        """Copies or sets necessary state attributes from the archetype card object."""
        # Derived classes will implement card type specific defaults
        pass

    # Zones whose contents are hidden knowledge even from their owner: nobody
    # may know their own deck order or prize card faces. The owner learns a
    # card's identity only when it legally becomes visible (EntityIntroduced
    # on draw); prize cards are never introduced until taken.
    HIDDEN_FROM_OWNER_AREAS = ("deck", "prizePile")

    def is_hidden_from(self, viewer_id: Optional[str]) -> bool:
        """A card's identity is hidden from non-owners always, and from its
        owner too while it sits in a hidden-knowledge zone (deck/prizes)."""
        if viewer_id is None:
            return False
        if viewer_id != self.owning_player_id:
            return True
        return (
            self.parent is not None
            and self.parent.get_attribute(AttrID.NAME) in self.HIDDEN_FROM_OWNER_AREAS
        )


class PokemonEntity(CardEntity):
    """Represents a Pokemon card entity on the board."""
    def _initialize_attributes(self):
        super()._initialize_attributes()
        hp_val = self.card_obj.get_attribute_value(AttrID.HP, 100)
        self.set_attribute(AttrID.HP, hp_val)
        self.attribute_originals[AttrID.HP.value] = hp_val

    def get_entity_name(self) -> str:
        return "com.direwolfdigital.cake.rules.entities.Pokemon"


class EnergyEntity(CardEntity):
    """Represents an Energy card entity on the board."""
    def get_entity_name(self) -> str:
        return "com.direwolfdigital.cake.rules.entities.Energy"


class TrainerEntity(CardEntity):
    """Represents a Trainer card entity on the board."""
    def get_entity_name(self) -> str:
        return "com.direwolfdigital.cake.rules.entities.TrainerCard"


def create_card_entity(card_obj: Card, owning_player_id: Optional[str] = None, entity_id: Optional[str] = None) -> CardEntity:
    """Factory function to build the correct subclass of CardEntity based on its card type."""
    c_type = card_obj.get_attribute_value(AttrID.CARD_TYPE)
    if c_type == CardType.POKEMON.value:
        return PokemonEntity(card_obj, owning_player_id, entity_id)
    elif c_type == CardType.ENERGY.value:
        return EnergyEntity(card_obj, owning_player_id, entity_id)
    else:
        return TrainerEntity(card_obj, owning_player_id, entity_id)


class BoardState:
    """Manages the full tree layout of the Playmat, keeping O(1) cache of all entities for rapid access."""
    def __init__(self, game_id: str, player_ids: List[str]):
        self.game_id: str = game_id
        self.player_ids: List[str] = player_ids
        
        # Build Playmat Root Entity
        self.playmat = PlayMat()
        
        # Internal cache map (entityID -> BoardEntity) for O(1) lookups
        self._entity_cache: Dict[str, BoardEntity] = {self.playmat.entity_id: self.playmat}
        
        self.game_options: Dict[str, Any] = {
            "theme": "ForestPlaymat"
        }
        # player_id -> prize cards dealt at setup; prizes taken = dealt - remaining.
        self.prizes_dealt: Dict[str, int] = {}
        # Set by GameSession once both exist; damage/condition lookups read it
        # defensively (getattr(board, "turn_state", None)) for bare test boards.
        self.turn_state = None

        self._initialize_board()

    def _register_entity(self, entity: BoardEntity):
        """Registers an entity and recursively its children in the lookup cache."""
        self._entity_cache[entity.entity_id] = entity
        for child in entity.children:
            self._register_entity(child)

    def _unregister_entity(self, entity: BoardEntity):
        """Unregisters an entity and recursively its children from the lookup cache."""
        if entity.entity_id in self._entity_cache:
            del self._entity_cache[entity.entity_id]
        for child in entity.children:
            self._unregister_entity(child)

    def get_entity(self, entity_id: str) -> Optional[BoardEntity]:
        """Retrieves an entity from the board by its entity ID in O(1) time."""
        return self._entity_cache.get(entity_id)

    def _initialize_board(self):
        """Sets up the initial board structures with global areas and player-specific areas."""
        # 1. Build Global Areas
        global_piles = ["outOfPlay", "activeStadium", "activeTrainer"]
        for pile_name in global_piles:
            area = PlayArea(pile_name)
            self.playmat.add_child(area)
            self._register_entity(area)

        # 2. Build Player Entities and their sub-areas
        player_piles = ["deck", "hand", "bench", "activePokemonArea", "discard", "prizePile", "lostZone"]
        for p_id in self.player_ids:
            player_entity = PlayerEntity(p_id)
            self.playmat.add_child(player_entity)
            self._register_entity(player_entity)

            for pile_name in player_piles:
                area = PlayArea(pile_name, owning_player_id=p_id)
                if pile_name == "bench":
                    # BenchLayout (client) spaces cards by dividing by this
                    # slot count (attr 201920 via the U.E facet); without it
                    # Slots reads 0 and every benched card gets a NaN
                    # transform (invisible card + collider crash).
                    area.set_attribute(AttrID.AREA_SLOTS, BENCH_SLOT_COUNT)
                player_entity.add_child(area)
                self._register_entity(area)

    def find_player_entity(self, player_id: str) -> Optional[PlayerEntity]:
        """Finds the PlayerEntity on the playmat for a given player ID."""
        for child in self.playmat.children:
            if isinstance(child, PlayerEntity) and child.owning_player_id == player_id:
                return child
        return None

    def find_player_area(self, player_id: str, area_name: str) -> Optional[PlayArea]:
        """Finds a specific play area for a given player ID (e.g., 'deck', 'hand')."""
        player_entity = self.find_player_entity(player_id)
        if player_entity:
            for sub_child in player_entity.children:
                if isinstance(sub_child, PlayArea) and sub_child.get_attribute(AttrID.NAME) == area_name:
                    return sub_child
        return None

    def find_global_area(self, area_name: str) -> Optional[PlayArea]:
        """Finds a global play area by its name (e.g., 'activeStadium')."""
        for child in self.playmat.children:
            if isinstance(child, PlayArea) and child.get_attribute(AttrID.NAME) == area_name:
                return child
        return None

    def add_card_to_area(self, card_entity: CardEntity, area: PlayArea):
        """Inserts a card entity into a play area, updating ownership and registration."""
        area.add_child(card_entity)
        card_entity.owning_player_id = area.owning_player_id
        self._register_entity(card_entity)

    def move_card(self, card_id: str, to_area_id: str, position: Optional[int] = None) -> bool:
        """Moves a card entity to a target play area, handling parent association gracefully."""
        card = self.get_entity(card_id)
        to_area = self.get_entity(to_area_id)

        if not isinstance(card, CardEntity) or not isinstance(to_area, PlayArea):
            return False

        if card.parent_id:
            parent = self.get_entity(card.parent_id)
            if parent:
                parent.remove_child(card)

        to_area.add_child(card, position)
        card.owning_player_id = to_area.owning_player_id
        return True

    def attach_card(self, card_id: str, to_entity_id: str) -> bool:
        """Reparents a card underneath another CARD entity (not a play area).

        This is how energy attachments and evolution stacks are modeled: the
        attached card becomes a child of the Pokemon entity, mirroring the
        client's entity tree where a pile's top card renders and its children
        ride along (energy pips, tools, previous stages).
        """
        card = self.get_entity(card_id)
        target = self.get_entity(to_entity_id)

        if not isinstance(card, CardEntity) or not isinstance(target, CardEntity):
            return False
        if card is target:
            return False

        if card.parent_id:
            parent = self.get_entity(card.parent_id)
            if parent:
                parent.remove_child(card)

        target.add_child(card)
        card.owning_player_id = target.owning_player_id
        return True

    def shuffle_deck(self, player_id: str, rng: Optional[random.Random] = None) -> bool:
        """Randomizes the order of the player's deck in place.
        """
        deck_area = self.find_player_area(player_id, "deck")
        if not deck_area:
            return False
        (rng or random).shuffle(deck_area.children)
        return True

    def deal_from_deck(self, player_id: str, area_name: str, count: int) -> List[Dict[str, Any]]:
        """Moves the top `count` cards from the player's deck into one of their areas.

        Returns move descriptors ({entity_id, destination_id, position, card})
        in deal order for building EntityMoved messages.
        """
        deck_area = self.find_player_area(player_id, "deck")
        dest_area = self.find_player_area(player_id, area_name)
        if not deck_area or not dest_area:
            return []

        moved: List[Dict[str, Any]] = []
        for _ in range(count):
            if not deck_area.children:
                break
            # Top of the deck is the last child (cards are appended when populated).
            card = deck_area.children[-1]
            position = len(dest_area.children)
            if not self.move_card(card.entity_id, dest_area.entity_id):
                break
            moved.append({
                "entity_id": card.entity_id,
                "destination_id": dest_area.entity_id,
                "position": position,
                "card": card,
            })
        if area_name == "prizePile" and moved:
            self.prizes_dealt[player_id] = self.prizes_dealt.get(player_id, 0) + len(moved)
        return moved

    def prizes_taken(self, player_id: str) -> int:
        """Prize cards the player has taken so far this game."""
        area = self.find_player_area(player_id, "prizePile")
        if not area:
            return 0
        return max(0, self.prizes_dealt.get(player_id, 0) - len(area.children))

    def draw_cards(self, player_id: str, count: int) -> List[Dict[str, Any]]:
        """Moves the top `count` cards from the player's deck into their hand."""
        return self.deal_from_deck(player_id, "hand", count)

    @staticmethod
    def _is_basic_pokemon(entity: BoardEntity) -> bool:
        return (
            isinstance(entity, PokemonEntity)
            and entity.card_obj.get_attribute_value(AttrID.STAGE) == PokemonStage.BASIC.value
        )

    def basic_pokemon_in_hand(self, player_id: str) -> List['PokemonEntity']:
        """All Basic Pokemon entities currently in the player's hand."""
        hand_area = self.find_player_area(player_id, "hand")
        if not hand_area:
            return []
        basics: List[PokemonEntity] = []
        for c in hand_area.children:
            if isinstance(c, PokemonEntity) and self._is_basic_pokemon(c):
                basics.append(c)
        return basics

    def has_basic_pokemon_in_hand(self, player_id: str) -> bool:
        """True if the player's hand contains at least one Basic Pokemon.

        A hand with no Basic Pokemon forces a mulligan in the setup phase.
        """
        return bool(self.basic_pokemon_in_hand(player_id))

    def player_has_any_basic(self, player_id: str) -> bool:
        """True if the player has a Basic Pokemon anywhere in deck or hand.

        Guards the mulligan loop against decks that can never produce a legal
        opening hand (which would otherwise reshuffle forever).
        """
        for area_name in ("deck", "hand"):
            area = self.find_player_area(player_id, area_name)
            if area and any(self._is_basic_pokemon(c) for c in area.children):
                return True
        return False

    def pokemon_in_play(self, player_id: str) -> List['PokemonEntity']:
        """The player's top-level Pokemon: the Active plus every benched one.

        Only direct children of the areas count -- cards stacked underneath a
        Pokemon (energy, tools, pre-evolutions) are attachments, not Pokemon
        in play.
        """
        in_play: List[PokemonEntity] = []
        for area_name in ("activePokemonArea", "bench"):
            area = self.find_player_area(player_id, area_name)
            for child in (area.children if area else []):
                if isinstance(child, PokemonEntity):
                    in_play.append(child)
        return in_play

    def active_pokemon(self, player_id: str) -> Optional['PokemonEntity']:
        """The player's Active Pokemon (top-level card of the active area)."""
        area = self.find_player_area(player_id, "activePokemonArea")
        for child in (area.children if area else []):
            if isinstance(child, PokemonEntity):
                return child
        return None

    def free_bench_slot(self, player_id: str) -> int:
        """Lowest bench slot not occupied by a current bench child's stamp.

        The client keeps every benched card at the slot it arrived in
        (positionInParent), leaving a gap when one is promoted/knocked out,
        so new arrivals must fill gaps instead of appending by list length.
        """
        bench = self.find_player_area(player_id, "bench")
        if not bench:
            return 0
        occupied = {self.bench_slot_of(c) for c in bench.children}
        for slot in range(BENCH_SLOT_COUNT):
            if slot not in occupied:
                return slot
        return len(bench.children)

    @staticmethod
    def bench_slot_of(entity: 'BoardEntity') -> int:
        """The slot the client renders this benched entity at (stamp, else list index)."""
        if entity.board_slot is not None:
            return entity.board_slot
        if entity.parent is not None and entity in entity.parent.children:
            return entity.parent.children.index(entity)
        return 0

    @staticmethod
    def attached_energies(pokemon: 'PokemonEntity') -> List['EnergyEntity']:
        """Every Energy card attached anywhere under a Pokemon's stack."""
        energies: List[EnergyEntity] = []
        stack: List[BoardEntity] = list(pokemon.children)
        while stack:
            entity = stack.pop()
            if isinstance(entity, EnergyEntity):
                energies.append(entity)
            stack.extend(entity.children)
        return energies

    def return_hand_to_deck(self, player_id: str):
        """Moves every card in the player's hand back into their deck (for a mulligan reshuffle)."""
        hand_area = self.find_player_area(player_id, "hand")
        deck_area = self.find_player_area(player_id, "deck")
        if not hand_area or not deck_area:
            return
        for card in list(hand_area.children):
            self.move_card(card.entity_id, deck_area.entity_id)

    def populate_deck(self, player_id: str, deck_data: Dict[str, Any]):
        """Decodes the player deck definition, pre-populates card entities, and updates player token attributes."""
        deck_area = self.find_player_area(player_id, "deck")
        if not deck_area:
            return

        actual_deck = deck_data.get("deck", deck_data)
        cards_list = actual_deck.get("cards", [])

        # Reconstruct cards from standard DB piles structure (supporting both 'deck' and client-serialized 'CakePile')
        if not cards_list and "piles" in actual_deck and isinstance(actual_deck["piles"], dict):
            piles_deck = None
            if "deck" in actual_deck["piles"]:
                piles_deck = actual_deck["piles"]["deck"]
            elif "CakePile" in actual_deck["piles"]:
                piles_deck = actual_deck["piles"]["CakePile"]

            if isinstance(piles_deck, list):
                counts = {}
                for guid in piles_deck:
                    if guid:
                        # Normalize GUID to lowercase to ensure match with loaders
                        counts[guid.lower()] = counts.get(guid.lower(), 0) + 1
                cards_list = [{"guid": g, "count": c} for g, c in counts.items()]

        has_gx = False
        has_vstar = False

        for card_item in cards_list:
            guid = card_item.get("guid")
            count = card_item.get("count", 1)

            if guid:
                card_obj = card_loader.cards_by_guid.get(guid.lower())
                if card_obj:
                    # Scan for GX and VSTAR card identifiers to set playmat tokens
                    stage = card_obj.get_attribute_value(AttrID.STAGE)
                    rarity = card_obj.get_attribute_value(AttrID.RARITY)
                    display_name = getattr(card_obj, "display_name", "") or ""
                    searchable = getattr(card_obj, "searchable_by", [])

                    if (
                        stage == PokemonStage.VSTAR.value or
                        rarity == Rarities.RareHoloVSTAR.value or
                        "VSTAR" in display_name or
                        any("vstar" in s.lower() for s in searchable)
                    ):
                        has_vstar = True

                    if (
                        rarity == Rarities.RareHoloGX.value or
                        "GX" in display_name or
                        "-GX" in display_name or
                        any("gx" in s.lower() for s in searchable)
                    ):
                        has_gx = True

                    for _ in range(count):
                        card_entity = create_card_entity(card_obj, owning_player_id=player_id)
                        self.add_card_to_area(card_entity, deck_area)
                else:
                    logging.warning(f"[BoardState] Failed to find card object for GUID: {guid}")

        # Dynamically attach playmat token visibility attributes to the PlayerEntity if present on the board
        player_entity = self.find_player_entity(player_id)
        if player_entity:
            player_entity.set_attribute(PlayerAttrID.HAS_GX_TOKEN, has_gx)
            player_entity.set_attribute(PlayerAttrID.HAS_VSTAR_TOKEN, has_vstar)
            logging.info(f"[BoardState] Set token flags for {player_id}: GX={has_gx}, VSTAR={has_vstar}")

    def _refresh_bench_gaps(self):
        """Syncs each bench's slot-order and AREA_EMPTY_SLOTS for SGS loads.

        Freshly loaded entities carry no A.m stamps, so the client lays the
        bench out sequentially, skipping the gaps listed in attr 201860.
        """
        for p_id in self.player_ids:
            bench = self.find_player_area(p_id, "bench")
            if not bench:
                continue
            bench.children.sort(key=self.bench_slot_of)
            occupied = {self.bench_slot_of(c) for c in bench.children}
            bench.set_attribute(
                AttrID.AREA_EMPTY_SLOTS,
                [s for s in range(BENCH_SLOT_COUNT) if s not in occupied],
            )

    def serialize(self, viewer_id: Optional[str] = None) -> Dict[str, Any]:
        """Builds the final SerializedGameState dict expected by the client network router.

        viewer_id scopes hidden information: cards not owned by the viewer are
        serialized un-introduced (attributes=null) so they render face-down.
        """
        self._refresh_bench_gaps()
        return {
            "messageName": OutboundMsg.SERIALIZED_GAME_STATE.value,
            "gameID": self.game_id,
            "playerAccounts": self.player_ids,
            "gameOptions": self.game_options,
            "entities": self.playmat.serialize(viewer_id)
        }
