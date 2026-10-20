from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cbbf7675-cd59-549e-a4e8-931ab70c1c82",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    display_name="Burmy",
    searchable_by=["Burmy", "Basic", "Burmy"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=412,
    abilities=[
        Attack(
            title="Hang Down",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)