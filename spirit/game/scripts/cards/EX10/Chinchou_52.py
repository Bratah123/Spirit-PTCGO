"""STUB: effect not implemented — do not guess mechanics.
Chinchou (EX10 #52): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="4ba9c9a8-0e38-5533-8d10-3546939c38e5",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    display_name="Chinchou",
    searchable_by=["Chinchou", "Basic", "Chinchou"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=170,
    abilities=[
        Attack(
            title="Thunder Wave",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)