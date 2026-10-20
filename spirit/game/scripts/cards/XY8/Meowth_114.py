"""STUB: effect not implemented — do not guess mechanics.
Meowth (XY8 #114): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2cdbd8bb-1be9-55bd-9f65-71c223b17161",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Exhausted Tackle",
            game_text="Flip a coin. If heads, this attack does 30 damage to your opponent's Active Pok\u00e9mon. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)