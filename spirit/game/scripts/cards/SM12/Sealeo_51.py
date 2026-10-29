from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1d22d375-cc21-59b3-b011-71ac97f3c953",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    display_name="Sealeo",
    searchable_by=["Sealeo", "Stage 1", "Sealeo"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Ice Ball",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)