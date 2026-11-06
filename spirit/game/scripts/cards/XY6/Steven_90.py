from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_supporter_card
from spirit.game.card_effects.trainers import is_basic_energy_card, deck_nonempty


async def steven(ctx):
    """Search your deck for a Supporter card and a basic Energy card, reveal
    them, and put them into your hand. Shuffle your deck afterward."""
    groups = await ctx.search_deck_groups(
        [(is_supporter_card, 1, "Supporter card"), (is_basic_energy_card, 1, "basic Energy card")],
        prompt="Choose a Supporter card and a basic Energy card")
    picks = [c for g in groups or [] for c in g]
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="1d911495-bac3-5000-b31b-4be666caca7e",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Steven.Name",
    display_name="Steven",
    searchable_by=["Steven", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=steven,
    condition=deck_nonempty
)
