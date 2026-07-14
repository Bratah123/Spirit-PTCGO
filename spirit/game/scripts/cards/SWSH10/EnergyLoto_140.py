from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_energy_card


async def energy_loto(ctx):
    """Look at the top 7 cards of your deck. You may reveal an Energy card
    you find there and put it into your hand. Shuffle the rest back."""
    top = ctx.deck_top(7)
    if top:
        candidates = [c for c in top if is_energy_card(c)]
        if candidates:
            picks = await ctx.choose_cards(
                candidates, 1, minimum=0,
                prompt="You may choose an Energy card to reveal and put into your hand.",
                display_cards=top if len(candidates) < len(top) else None,
            )
            await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="d1eb2cba-088d-50de-936d-623ac279b013",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyLoto.Name",
    display_name="Energy Loto",
    searchable_by=["Energy Loto", "Item"],
    subtypes=["Item"],
    collector_number=140,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=energy_loto,
)
