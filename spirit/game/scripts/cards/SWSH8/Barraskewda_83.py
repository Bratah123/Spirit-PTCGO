from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c2a5dbb8-5012-5a05-be03-ab0de4f355cd",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barraskewda.Name",
    display_name="Barraskewda",
    searchable_by=["Barraskewda", "Stage 1", "Barraskewda"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    family_id=846,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.WATER: 1},
            damage=50,
        ),
    ],
)