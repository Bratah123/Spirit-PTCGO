from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import count_prizes_remaining

_opponent_prizes_remaining = count_prizes_remaining("opponent")


async def schoolgirl(ctx):
    await ctx.draw_cards(2)
    if _opponent_prizes_remaining(ctx) in (2, 4, 6):
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="e4635c23-a848-5c8b-9f6d-2fdeda500876",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Schoolgirl.Name",
    display_name="Schoolgirl",
    searchable_by=["Schoolgirl", "Supporter"],
    subtypes=["Supporter"],
    collector_number=262,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    effect=schoolgirl
)
