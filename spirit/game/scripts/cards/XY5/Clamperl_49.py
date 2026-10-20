"""STUB: effect not implemented — do not guess mechanics.
Clamperl (XY5 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e0193a99-0d26-513b-8328-498e4151e5a5",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    display_name="Clamperl",
    searchable_by=["Clamperl", "Basic", "Clamperl"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=366,
    abilities=[
        Attack(
            title="Shell Protection",
            game_text="During your opponent's next turn, if this Pok\u00e9mon would be damaged by an attack, prevent that attack's damage done to this Pok\u00e9mon if that damage is 50 or less.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)