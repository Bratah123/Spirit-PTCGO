from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.session.effects import is_trainer_card


async def oleana_effect(ctx):
    """Discard 2 other cards, then your opponent reveals their hand and you
    put a Trainer card found there on the bottom of their deck."""
    discarded = await ctx.discard_from_hand(
        2, prompt="Discard 2 cards to play Oleana",
    )
    if len(discarded) < 2:
        return
    opp_hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    trainers = [c for c in opp_hand if is_trainer_card(c)]
    if not trainers:
        return
    picks = await ctx.choose_cards(
        trainers, 1, minimum=1, display_cards=opp_hand,
        prompt="Choose a Trainer card to put on the bottom of your opponent's deck",
    )
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)


card = SupporterCardDef(
    guid="afebe747-65b2-5600-acae-30e507332bb1",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Oleana.Name",
    display_name="Oleana",
    searchable_by=["Oleana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=202,
    set_code="SWSH2",
    rarity=Rarities.RareRainbow,
    effect=oleana_effect,
    condition=requires_hand(n=2),
)
