from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon, is_water_pokemon
from spirit.game.card_effects.support_common import search_to_bench


def _is_basic_water_pokemon(card):
    return is_basic_pokemon(card) and is_water_pokemon(card)


card = PokemonCardDef(
    guid="ee7cc6fb-017d-5745-8653-bd3f2aa6464b",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic", "Phione"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=489,
    abilities=[
        Attack(
            title="Sea Feast",
            game_text="Search your deck for up to 3 Basic Water Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_bench(predicate=_is_basic_water_pokemon, count=3),
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
