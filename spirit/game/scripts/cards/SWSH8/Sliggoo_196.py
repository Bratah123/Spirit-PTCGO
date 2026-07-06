from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f934a0f6-8152-53a6-883a-1e95516f50c5",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    display_name="Sliggoo",
    searchable_by=["Sliggoo", "Stage 1", "Sliggoo"],
    subtypes=["Stage 1"],
    collector_number=196,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    family_id=704,
    abilities=[
        Attack(
            title="Melt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)