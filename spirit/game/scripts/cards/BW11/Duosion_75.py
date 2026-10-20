from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d1f767c3-ed5d-5ec3-8dc9-06b927bfa9c1",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    display_name="Duosion",
    searchable_by=["Duosion", "Stage 1", "Duosion"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name",
    family_id=577,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)