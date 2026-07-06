from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ac9b6e2c-911e-5cd0-8015-ff1b0c54b1bc",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    display_name="Impidimp",
    searchable_by=["Impidimp", "Basic", "Impidimp"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=859,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Stampede",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)