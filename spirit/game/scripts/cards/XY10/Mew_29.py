from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card, is_basic_pokemon
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.content.definitions import def_for


class _MemoriesOfDawn(Passive):
    """This Pokemon can use the attacks of any of your Basic Pokemon in play."""
    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        attacks, seen = [], set()
        for p in board.pokemon_in_play(pokemon.owning_player_id):
            if p is pokemon or not is_basic_pokemon(p) or p.archetype_id == pokemon.archetype_id:
                continue
            for a in getattr(def_for(p.archetype_id), "abilities", None) or []:
                if isinstance(a, Attack) and id(a) not in seen:
                    seen.add(id(a))
                    attacks.append(a)
        return attacks


card = PokemonCardDef(
    guid="ad6f8038-1236-513e-879b-ea7dcd1b7d1c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Memories of Dawn",
            game_text="This Pok\u00e9mon can use the attacks of any of your Basic Pok\u00e9mon in play. (You still need the necessary Energy to use each attack.)",
            passive=_MemoriesOfDawn(),
        ),
        Attack(
            title="Encounter",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_pokemon_card, count=1, minimum=0, reveal=True, prompt='Choose a Pokémon'),
        ),
    ],
)