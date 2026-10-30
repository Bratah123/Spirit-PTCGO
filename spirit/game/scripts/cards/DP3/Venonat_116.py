"""STUB: effect not implemented — do not guess mechanics.
Venonat (DP3 #116): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="23c9db82-ddab-55ff-afb6-1e629d0de7fc",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    display_name="Venonat",
    searchable_by=["Venonat", "Basic", "Venonat"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=48,
    abilities=[
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Signal Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)