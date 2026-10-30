from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6457f67b-17ed-523a-a72a-4305df7d2f59",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic", "Porygon"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Sharpen",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)