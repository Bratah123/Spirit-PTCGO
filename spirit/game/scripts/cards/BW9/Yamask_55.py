from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="641a3a80-bccd-5e8c-9ccb-c8abc001da6b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic", "Yamask"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=562,
    abilities=[
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)