from spirit.game.card_effects.ex import spiny_on_damaged
"""STUB: effect not implemented — do not guess mechanics.
Qwilfish (EX7 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    passive=spiny_on_damaged(),
    guid="3d883092-dca7-5016-8707-36aa74afcd68",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name",
    display_name="Qwilfish",
    searchable_by=["Qwilfish", "Basic", "Qwilfish"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=211,
    abilities=[
        Ability(
            title="Spiny",
            game_text="If Qwilfish is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Qwilfish is Knocked Out), flip a coin until you get tails. For each heads, put 1 damage counter on the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Stun Poison",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, SpecialConditions.POISONED, flip=True),
        ),
    ],
)