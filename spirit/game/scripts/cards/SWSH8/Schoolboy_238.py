from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import count_prizes_remaining

_opponent_prizes_remaining = count_prizes_remaining("opponent")


async def schoolboy(ctx):
    await ctx.draw_cards(2)
    if _opponent_prizes_remaining(ctx) in (1, 3, 5):
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="16e7d311-6731-5028-9de4-6421cad76f49",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Schoolboy.Name",
    display_name="Schoolboy",
    searchable_by=["Schoolboy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=238,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=schoolboy
)
