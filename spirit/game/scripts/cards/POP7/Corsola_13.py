from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import rally_bench_different_types

card = PokemonCardDef(
    guid="a4f7ea18-485f-55e9-b139-5916269d078e",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name",
    display_name="Corsola",
    searchable_by=['Corsola', 'Basic', 'Corsola'],
    subtypes=["Basic"],
    collector_number=13,
    set_code="POP7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=222,
    abilities=[
        Attack(
            title="Rally",
            game_text="Search your deck for up to 3 different types of Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rally_bench_different_types(3),
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
