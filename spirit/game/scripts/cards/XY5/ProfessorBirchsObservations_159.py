from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def professor_birchs_observations(ctx):
    """Shuffle your hand into your deck; flip: heads draw 7, tails draw 4."""
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    else:
        await ctx.shuffle_deck()
    results = await ctx.flip_coins(1, "Professor Birch's Observations")
    await ctx.draw_cards(7 if results and results[0] else 4)


card = SupporterCardDef(
    guid="cc26edad-ecc7-55b9-b7c5-ff405493cea1",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirchsObservations.Name",
    display_name="Professor Birch's Observations",
    searchable_by=["Professor Birch's Observations", "Supporter"],
    subtypes=["Supporter"],
    collector_number=159,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    effect=professor_birchs_observations
)
