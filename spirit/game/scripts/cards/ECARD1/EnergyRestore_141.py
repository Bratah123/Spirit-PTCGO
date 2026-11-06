from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def energy_restore(ctx):
    """Flip 3 coins; for each heads recover a basic Energy from discard to hand."""
    results = await ctx.flip_coins(3, "Energy Restore")
    heads = sum(1 for r in results if r)
    if heads <= 0:
        return
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not pool:
        return
    count = min(heads, len(pool))
    picks = await ctx.choose_cards(
        pool, count,
        prompt=f"Choose {count} basic Energy card(s) to put into your hand",
    )
    if picks:
        await ctx.put_in_hand(picks)


card = ItemCardDef(
    guid="ff947b34-c2be-5a79-918c-f3faa70d4735",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRestore.Name",
    display_name="Energy Restore",
    searchable_by=["Energy Restore"],
    subtypes=[],
    collector_number=141,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=energy_restore,
)
