from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c26c56ae-fc37-510b-a37a-8dadfe836378",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    display_name="Petilil",
    searchable_by=["Petilil", "Basic", "Petilil"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=548,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)