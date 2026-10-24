from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least, is_basic_energy_card


async def superior_energy_retrieval(ctx):
    """Discard 2 cards from your hand (required), then put 4 basic Energy
    cards from your discard pile into your hand; the cards just discarded
    can't be chosen."""
    gone = await ctx.discard_from_hand(2, minimum=2, prompt="Discard 2 cards for Superior Energy Retrieval")
    if len(gone or []) < 2:
        return
    just = {c.entity_id for c in gone}
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c) and c.entity_id not in just]
    n = min(4, len(pool))
    if n <= 0:
        return
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 4 basic Energy cards to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = ItemCardDef(
    guid="9db709ce-a606-5210-9ce4-1f99b8591184",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperiorEnergyRetrieval.Name",
    display_name="Superior Energy Retrieval",
    searchable_by=["Superior Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=103,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=superior_energy_retrieval,
    condition=hand_size_at_least(3)
)
