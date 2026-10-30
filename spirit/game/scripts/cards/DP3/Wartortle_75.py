"""STUB: effect not implemented — do not guess mechanics.
Wartortle (DP3 #75): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9a287abd-d18b-50ed-a64c-4ba03132b4cb",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    display_name="Wartortle",
    searchable_by=["Wartortle", "Stage 1", "Wartortle"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Giant Wave",
            game_text="Wartortle can't use Giant Wave during your next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shell Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)