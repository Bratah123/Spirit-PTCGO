from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c72e9289-2ed6-5e10-b81b-becf4a43fce1",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    display_name="Fennekin",
    searchable_by=["Fennekin", "Basic", "Fennekin"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=653,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)