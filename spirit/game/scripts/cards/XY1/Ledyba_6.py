from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab090fef-50e6-509c-b9a4-dd7dd9bda1d2",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    display_name="Ledyba",
    searchable_by=["Ledyba", "Basic", "Ledyba"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=165,
    abilities=[
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)