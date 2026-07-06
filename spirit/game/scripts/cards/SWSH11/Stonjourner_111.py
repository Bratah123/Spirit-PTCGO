from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f5472cf-1f35-562d-af9d-7372d55adcb8",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name",
    display_name="Stonjourner",
    searchable_by=["Stonjourner", "Basic", "Stonjourner"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=874,
    abilities=[
        Attack(
            title="Power Stone",
            game_text="Attach up to 2 Fighting Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Lost Shot",
            game_text="Put the top card of your opponent's deck in the Lost Zone.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)