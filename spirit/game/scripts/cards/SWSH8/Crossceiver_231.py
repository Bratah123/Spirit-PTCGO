from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card, is_supporter_card


def _named(card, name):
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == name


def _playable(board, player_id, card):
    """Needs a 2nd Crossceiver in hand and a Pokemon/Supporter in the discard."""
    hand = board.find_player_area(player_id, "hand")
    has_pair = any(c.entity_id != card.entity_id and _named(c, "Crossceiver")
                   for c in (hand.children if hand else []))
    discard = board.find_player_area(player_id, "discard")
    has_target = any(is_pokemon_card(c) or is_supporter_card(c)
                     for c in (discard.children if discard else []))
    return has_pair and has_target


async def crossceiver(ctx):
    """Play 2 at once: discard the 2nd copy, then put a Pokemon or a Supporter
    from your discard pile into your hand."""
    pair = next((c for c in ctx.hand()
                 if c.entity_id != ctx.source.entity_id
                 and _named(c, "Crossceiver")), None)
    if pair is None:
        return
    await ctx.discard_cards([pair])
    candidates = [c for c in ctx.discard_pile()
                  if is_pokemon_card(c) or is_supporter_card(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Pokémon or a Supporter card to put into your hand.",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = ItemCardDef(
    guid="e82e24fb-7322-5f44-8cb1-fe5e9b9cd43a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Crossceiver.Name",
    display_name="Crossceiver",
    searchable_by=["Crossceiver", "Item", "Fusion Strike"],
    subtypes=["Item", "Fusion Strike"],
    collector_number=231,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    condition=_playable,
    effect=crossceiver,
)
