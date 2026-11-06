from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def hand_scope(ctx):
    """Your opponent reveals their hand."""
    await ctx.reveal_hand(ctx.opponent_id)


card = ItemCardDef(
    guid="90f305ed-6ccb-5e8a-9a38-23aa6cc73527",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HandScope.Name",
    display_name="Hand Scope",
    searchable_by=["Hand Scope", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=hand_scope
)
