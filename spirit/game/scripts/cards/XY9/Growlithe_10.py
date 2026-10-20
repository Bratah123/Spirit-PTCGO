from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a4da4d81-efcb-5454-9d26-610a69a76165",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic", "Growlithe"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)