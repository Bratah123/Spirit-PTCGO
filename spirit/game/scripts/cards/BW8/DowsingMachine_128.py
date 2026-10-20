from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least
from spirit.game.session.effects import is_trainer_card


async def dowsing_machine(ctx):
    """ACE SPEC: discard 2 cards from your hand, then put a Trainer card from
    your discard pile into your hand."""
    if len(await ctx.discard_from_hand(2, prompt="Discard 2 cards for Dowsing Machine")) < 2:
        return
    pool = [c for c in ctx.discard_pile() if is_trainer_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Trainer card to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = ItemCardDef(
    guid="b5f85814-dbe1-5495-bcda-cdee9d7f4442",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DowsingMachine.Name",
    display_name="Dowsing Machine",
    searchable_by=["Dowsing Machine", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=128,
    set_code="BW8",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=dowsing_machine,
    condition=hand_size_at_least(3)
)
