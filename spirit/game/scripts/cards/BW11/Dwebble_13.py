from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2cbccc14-1af6-524b-8580-b0e27a0256e6",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    display_name="Dwebble",
    searchable_by=["Dwebble", "Basic", "Dwebble"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=557,
    abilities=[
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)