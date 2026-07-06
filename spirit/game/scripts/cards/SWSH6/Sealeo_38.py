from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="72477367-76aa-5e8a-bcbf-6aa9e744bf4f",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    display_name="Sealeo",
    searchable_by=["Sealeo", "Stage 1", "Sealeo"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)