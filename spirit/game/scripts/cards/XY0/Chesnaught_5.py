"""STUB: effect not implemented — do not guess mechanics.
Chesnaught (XY0 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ec9ecc4b-8509-5770-ac48-14790cd78696",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chesnaught.Name",
    display_name="Chesnaught",
    searchable_by=["Chesnaught", "Stage 2", "Chesnaught"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name",
    family_id=650,
    abilities=[
        Attack(
            title="Needle Arm",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)