"""STUB: effect not implemented — do not guess mechanics.
Jynx (SL #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
import random
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def astonish(ctx):
    """Choose a random card from the opponent's hand, reveal it, shuffle into their deck."""
    await ctx.deal_damage()
    opponent = ctx.opponent_id
    hand = ctx.hand(opponent)
    if not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card])
    await ctx.shuffle_into_deck([card], player_id=opponent)


card = PokemonCardDef(
    guid="ad272926-8d37-5c81-a323-ae2ed4dd3ead",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="SL",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Attack(
            title="Whiny Voice",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=astonish,
        ),
        Attack(
            title="Feverish Kiss",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)