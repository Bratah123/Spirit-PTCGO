from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.support_common import look_at_top


def _is_fire_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIRE.value in types


def _kindler_condition(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_fire_energy_card(c) for c in hand.children)


async def kindler(ctx):
    """Discard a Fire Energy from hand, then look at top 7 for up to 2 to hand."""
    discarded = await ctx.discard_from_hand(
        1, predicate=_is_fire_energy_card, prompt="Discard a Fire Energy card"
    )
    if not discarded:
        return
    await look_at_top(7, take=2, rest="shuffle", minimum=0)(ctx)


card = SupporterCardDef(
    guid="fb1e692d-aa85-55f1-8cf8-62d0569032d3",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kindler.Name",
    display_name="Kindler",
    searchable_by=["Kindler", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    condition=_kindler_condition,
    effect=kindler,
)
