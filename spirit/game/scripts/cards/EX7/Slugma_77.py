from spirit.game.card_effects.ex import heat_tackle_self
"""STUB: effect not implemented — do not guess mechanics.
Slugma (EX7 #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="541d614a-08cf-5a30-b303-153aad747a2a",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic", "Slugma"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Singe",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
        Attack(
            title="Heat Tackle",
            game_text="Slugma does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=heat_tackle_self(),
        ),
    ],
)