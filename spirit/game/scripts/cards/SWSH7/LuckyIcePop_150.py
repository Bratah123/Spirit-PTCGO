from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def lucky_ice_pop_effect(ctx):
    """Heal 20 from your Active; if any damage was healed, flip - heads returns
    this card to hand instead of the discard pile."""
    healed = await ctx.heal(20)
    if healed <= 0:
        return
    heads = (await ctx.flip_coins(1, "Lucky Ice Pop"))[0]
    if heads:
        await ctx.put_in_hand([ctx.source], reveal=False)


card = ItemCardDef(
    guid="f4b60669-ccfa-5017-8a9c-0f9a84b2ba98",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyIcePop.Name",
    display_name="Lucky Ice Pop",
    searchable_by=["Lucky Ice Pop", "Item"],
    subtypes=["Item"],
    collector_number=150,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    effect=lucky_ice_pop_effect
)
