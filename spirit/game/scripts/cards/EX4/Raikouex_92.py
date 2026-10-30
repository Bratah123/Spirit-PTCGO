"""STUB: effect not implemented — do not guess mechanics.
Raikou ex (EX4 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, recoil_attack


card = PokemonCardDef(
    guid="136c4634-3b98-5de2-aa24-e1ebfc2852f9",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikouex.Name",
    display_name="Raikou ex",
    searchable_by=["Raikou ex", "Basic", "ex", "Raikouex"],
    subtypes=["Basic", "ex"],
    collector_number=92,
    set_code="EX4",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Dazzle Blast",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Lightning Tackle",
            game_text="Flip a coin. If tails, Raikou ex does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=recoil_attack(20),
        ),
    ],
)