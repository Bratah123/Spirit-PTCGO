from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_energy_card


async def power_charge(ctx):
    """Flip heads → shuffle up to 2 Energy from discard into deck."""
    results = await ctx.flip_coins(1, "Power Charge")
    if not results or not results[0]:
        return
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if not pool:
        return
    count = min(2, len(pool))
    picks = await ctx.choose_cards(
        pool, count,
        prompt=f"Choose {count} Energy card(s) to shuffle into your deck",
    )
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


card = ItemCardDef(
    guid="56208084-623c-554a-821e-d1c9334e0ac6",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerCharge.Name",
    display_name="Power Charge",
    searchable_by=["Power Charge"],
    subtypes=[],
    collector_number=147,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=power_charge,
)
