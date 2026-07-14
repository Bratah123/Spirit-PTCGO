from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_trainer_card


async def acerolas_premonition(ctx):
    """Opponent reveals their hand; draw a card for each Trainer card found there."""
    cards = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    count = sum(1 for c in cards if is_trainer_card(c))
    if count:
        await ctx.draw_cards(count)


card = SupporterCardDef(
    guid="0c386ba6-db75-5ec7-9d70-0d55188018a6",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcerolasPremonition.Name",
    display_name="Acerola's Premonition",
    searchable_by=["Acerola's Premonition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=129,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    effect=acerolas_premonition
)
