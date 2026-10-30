"""STUB: effect not implemented — do not guess mechanics.
Chikorita δ (EX15 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="e2653f01-4535-5a0a-ae1c-f02e6bc3fbe2",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    display_name="Chikorita δ",
    searchable_by=["Chikorita \u03b4", "Basic", "Chikorita"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=152,
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)