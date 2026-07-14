from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


async def _put_discard_card_in_hand(ctx):
    discard = ctx.discard_pile()
    if not discard:
        return
    picks = await ctx.choose_cards(
        discard, 1, minimum=1, prompt="Choose a card to put into your hand",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = ItemCardDef(
    guid="3279662b-8876-5b8b-a540-ff9da908bb21",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldPC.Name",
    display_name="Old PC",
    searchable_by=["Old PC", "Item"],
    subtypes=["Item"],
    collector_number=164,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    effect=flip_or_nothing(coins=2, then=_put_discard_card_in_hand),
)
