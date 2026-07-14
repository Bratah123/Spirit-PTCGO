from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench

card = PokemonCardDef(
    guid="ea73bad4-a7bf-57f2-90e8-ff01f0d564b2",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculin.Name",
    display_name="Hisuian Basculin",
    searchable_by=["Hisuian Basculin", "Basic", "HisuianBasculin"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=550,
    abilities=[
        Attack(
            title="Gather the Crew",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={},
            effect=search_to_bench(count=2),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)