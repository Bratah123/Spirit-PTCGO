from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.passives import Passive
from spirit.game.content.definitions import def_for


class _MetamorphosisGene(Passive):
    """While this Pokemon is Active it can use the attacks of the opponent's
    Active Pokemon (Energy costs still apply)."""
    def granted_attacks(self, board, pokemon, carrier):
        if carrier is not pokemon or board.active_pokemon(pokemon.owning_player_id) is not pokemon:
            return []
        foe_id = next((pid for pid in board.player_ids if pid != pokemon.owning_player_id), None)
        foe = board.active_pokemon(foe_id) if foe_id else None
        if foe is None:
            return []
        return [a for a in (getattr(def_for(foe.archetype_id), "abilities", None) or [])
                if isinstance(a, Attack)]


card = PokemonCardDef(
    guid="ad9d7205-fd76-5fda-80c2-6f9cddae0abe",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Metamorphosis Gene",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, it can use the attacks of your opponent's Active Pok\u00e9mon. (You still need the necessary Energy to use each attack.)",
            passive=_MetamorphosisGene(),
        ),
        Attack(
            title="Stick On",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=attach_from_discard(predicate=is_basic_energy_card, count=1, target='self', prompt='Choose a basic Energy card to attach.'),
        ),
    ],
)