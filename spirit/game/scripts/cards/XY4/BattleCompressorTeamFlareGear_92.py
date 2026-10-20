from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty


async def battle_compressor(ctx):
    """Search your deck for up to 3 cards and discard them. Shuffle."""
    picks = await ctx.search_deck(lambda c: True, count=3, minimum=0,
                                  prompt="Choose up to 3 cards to discard")
    if picks:
        await ctx.discard_cards(picks)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="2af80aaa-b14a-5472-8a4f-6906f780a5a7",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleCompressorTeamFlareGear.Name",
    display_name="Battle Compressor Team Flare Gear",
    searchable_by=["Battle Compressor Team Flare Gear", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=battle_compressor,
    condition=deck_nonempty
)
