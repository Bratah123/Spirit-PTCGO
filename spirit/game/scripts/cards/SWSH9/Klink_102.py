from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f251c335-cc90-5869-990b-1d0add00e118",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    display_name="Klink",
    searchable_by=["Klink", "Basic", "Klink"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=599,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)