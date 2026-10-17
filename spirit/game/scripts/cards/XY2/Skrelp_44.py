"""STUB: effect not implemented — do not guess mechanics.
Skrelp (XY2 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3f0add16-1668-56c8-b576-59975d8a5f1c",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    display_name="Skrelp",
    searchable_by=["Skrelp", "Basic", "Skrelp"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=690,
    abilities=[
        Attack(
            title="Spit Poison",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)