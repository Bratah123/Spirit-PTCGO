"""STUB: effect not implemented — do not guess mechanics.
Larvitar δ (EX15 #52): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="be7f7d7e-3adb-5222-a53c-123ef94e3a56",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    display_name="Larvitar δ",
    searchable_by=["Larvitar \u03b4", "Basic", "Larvitar"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=246,
    abilities=[
        Attack(
            title="Paralyzing Gaze",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)