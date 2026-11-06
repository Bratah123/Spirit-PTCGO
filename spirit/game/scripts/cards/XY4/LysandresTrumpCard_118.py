from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for


def _not_trump_card(card):
    return getattr(def_for(card.archetype_id), "display_name", None) != "Lysandre's Trump Card"


async def lysandres_trump_card(ctx):
    """Each player shuffles all cards in their discard pile into their deck
    (except for Lysandre's Trump Card)."""
    for pid in (ctx.player_id, ctx.opponent_id):
        cards = [c for c in ctx.discard_pile(pid) if _not_trump_card(c)]
        if cards:
            await ctx.shuffle_into_deck(cards, pid)
        else:
            await ctx.shuffle_deck(pid)


card = SupporterCardDef(
    guid="dafac91a-ca68-5667-8a1f-f518503823e8",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandresTrumpCard.Name",
    display_name="Lysandre's Trump Card",
    searchable_by=["Lysandre's Trump Card", "Supporter"],
    subtypes=["Supporter"],
    collector_number=118,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    effect=lysandres_trump_card
)
