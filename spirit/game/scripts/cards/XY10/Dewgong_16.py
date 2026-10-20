"""STUB: effect not implemented — do not guess mechanics.
Dewgong (XY10 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd61f446-997e-52bc-beac-185d45eae92d",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Attack(
            title="Freezing Breath",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed. If tails, your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)