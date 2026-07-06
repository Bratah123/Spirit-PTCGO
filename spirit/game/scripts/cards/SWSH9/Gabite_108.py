from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="21a0da13-2c8f-5a1b-b0c2-aa8c3fe2c554",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    display_name="Gabite",
    searchable_by=["Gabite", "Stage 1", "Gabite"],
    subtypes=["Stage 1"],
    collector_number=108,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
        ),
    ],
)