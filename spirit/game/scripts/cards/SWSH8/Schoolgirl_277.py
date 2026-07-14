from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import count_prizes_remaining

_opponent_prizes_remaining = count_prizes_remaining("opponent")


async def schoolgirl(ctx):
    await ctx.draw_cards(2)
    if _opponent_prizes_remaining(ctx) in (2, 4, 6):
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="965bad7d-170a-5af0-b7f4-135f438752a0",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Schoolgirl.Name",
    display_name="Schoolgirl",
    searchable_by=["Schoolgirl", "Supporter"],
    subtypes=["Supporter"],
    collector_number=277,
    set_code="SWSH8",
    rarity=Rarities.RareRainbow,
    effect=schoolgirl
)
