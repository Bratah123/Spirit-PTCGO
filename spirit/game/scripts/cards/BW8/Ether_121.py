from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


def _deck_not_empty(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def ether(ctx):
    """Reveal the top card of your deck. If it is a basic Energy card, attach
    it to 1 of your Pokemon; otherwise return it to the top of your deck."""
    top = ctx.deck_top(1)
    if not top:
        return
    await ctx.reveal_cards(top)
    if not is_basic_energy_card(top[0]):
        return
    pool = ctx.my_pokemon_in_play()
    target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Choose a Pokémon to attach it to")
    await ctx.attach_energy(top[0], target or pool[0])


card = ItemCardDef(
    guid="6473890b-a3b0-5b3b-9d93-1a3e49321e7f",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ether.Name",
    display_name="Ether",
    searchable_by=["Ether", "Item"],
    subtypes=["Item"],
    collector_number=121,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=ether,
    condition=_deck_not_empty
)
