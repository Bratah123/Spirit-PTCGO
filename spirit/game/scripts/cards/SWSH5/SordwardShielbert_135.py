from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_trainer_card
from spirit.game.card_effects.support_common import requires_discard


async def _sordward_shielbert(ctx):
    discard = [c for c in ctx.discard_pile() if is_trainer_card(c)]
    if not discard:
        return
    picks = await ctx.choose_cards(
        discard, 1, minimum=1, prompt="Choose a Trainer card from your discard pile.",
    )
    if not picks:
        return
    if await ctx.ask_yes_no(
        "Your opponent chose a Trainer card from their discard pile. May they put it into their hand?",
        player_id=ctx.opponent_id,
    ):
        await ctx.put_in_hand(picks, reveal=False)
    else:
        await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="00d3fea6-aaa9-50dc-9a72-2ea453067678",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SordwardShielbert.Name",
    display_name="Sordward & Shielbert",
    searchable_by=["Sordward & Shielbert", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    condition=requires_discard(is_trainer_card),
    effect=_sordward_shielbert,
)
