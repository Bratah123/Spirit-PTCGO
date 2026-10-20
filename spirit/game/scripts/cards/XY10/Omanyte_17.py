from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="036d3cca-9ce1-5ec3-b0b3-0f31f54abb61",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    display_name="Omanyte",
    searchable_by=["Omanyte", "Restored", "Omanyte"],
    subtypes=["Restored"],
    collector_number=17,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HelixFossilOmanyte.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
    ],
)