"""STUB: effect not implemented — do not guess mechanics.
Qwilfish (DP3 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="776f1cb4-2fbf-5f58-9e59-9e514bd17946",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name",
    display_name="Qwilfish",
    searchable_by=["Qwilfish", "Basic", "Qwilfish"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=211,
    abilities=[
        Ability(
            title="Balloon Sting",
            game_text="Once during your opponent's turn, if Qwilfish is your Active Pok\u00e9mon and is damage by an attack (even if Qwilfish is Knocked Out), you may flip a coin. If heads, the Attacking Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Nerve Shot",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)