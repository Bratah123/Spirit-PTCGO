"""STUB: effect not implemented — do not guess mechanics.
Houndour (EX10 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="66c04edf-1b5b-5eb5-a645-b18c489fb31f",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    display_name="Houndour",
    searchable_by=["Houndour", "Basic", "Houndour"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=228,
    abilities=[
        Attack(
            title="Smog",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)