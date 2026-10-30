from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import (
    has_basic_energy_in_discard,
    is_basic_energy_card,
)


async def energy_restore(ctx):
    """Flip 3 coins. For each heads, put a basic Energy from discard into hand."""
    results = await ctx.flip_coins(3, "Energy Restore")
    heads = sum(1 for r in results if r)
    if heads:
        await recover_from_discard(
            is_basic_energy_card, count=heads, minimum=None,
            prompt="Choose Basic Energy cards to put into your hand.",
        )(ctx)


card = ItemCardDef(
    guid="8cd8946f-ab9b-58d5-9933-247457900a71",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRestore.Name",
    display_name="Energy Restore",
    searchable_by=["Energy Restore", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    condition=has_basic_energy_in_discard,
    effect=energy_restore,
)
