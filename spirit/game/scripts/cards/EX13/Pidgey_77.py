from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fd8243dd-45f3-5689-bf4e-6300cfacafc3",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    display_name="Pidgey δ",
    searchable_by=["Pidgey \u03b4", "Basic", "Pidgey"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=16,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)