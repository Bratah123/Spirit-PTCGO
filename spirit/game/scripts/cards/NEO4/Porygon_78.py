from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ebd8e945-ad03-5bf6-8dd3-0c6e97dcc95e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic", "Porygon"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=137,
    abilities=[
        Attack(
            title="Sharpen",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)