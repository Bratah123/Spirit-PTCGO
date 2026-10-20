from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93cf61d1-cd76-548c-aea6-0fed746cb6f9",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    display_name="Duosion",
    searchable_by=["Duosion", "Stage 1", "Duosion"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="BW3",
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