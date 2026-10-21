from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def psychics_third_eye(ctx):
    """Your opponent reveals their hand. Discard any number of cards from your hand, then draw that many."""
    if ctx.hand(ctx.opponent_id):
        await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if not hand:
        return
    picks = await ctx.choose_cards(hand, len(hand), minimum=0, prompt="Discard any number of cards")
    if picks:
        n = len(picks)
        await ctx.discard_cards(picks)
        await ctx.draw_cards(n)


card = SupporterCardDef(
    guid="c0c48f4f-0d69-5b91-af3f-1f25caf3e771",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PsychicsThirdEye.Name",
    display_name="Psychic's Third Eye",
    searchable_by=["Psychic's Third Eye", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=psychics_third_eye
)
