from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ed3c8e6-c94f-53ed-b541-1dd92e943299",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    display_name="Grubbin",
    searchable_by=["Grubbin", "Basic", "Grubbin"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=736,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)