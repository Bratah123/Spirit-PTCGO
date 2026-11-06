from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="91cb0a78-196e-505b-ad6a-90bffdd4f684",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    display_name="Sealeo",
    searchable_by=["Sealeo", "Stage 1", "Sealeo"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Ice Ball",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)