"""STUB: effect not implemented — do not guess mechanics.
Fletchinder (XY2 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2568632c-1702-5dcb-a8b2-88707a919963",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    display_name="Fletchinder",
    searchable_by=["Fletchinder", "Stage 1", "Fletchinder"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Firebreathing",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)