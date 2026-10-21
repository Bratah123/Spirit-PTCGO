from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


async def buddy_buddy_rescue(ctx):
    """Each player puts a Pokemon from their discard pile into their hand
    (your opponent chooses first)."""
    for pid in (ctx.opponent_id, ctx.player_id):
        pool = [c for c in ctx.discard_pile(pid) if is_pokemon_card(c)]
        if not pool:
            continue
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Pokémon to put into your hand",
                                       player_id=pid)
        if picks:
            await ctx.put_in_hand(picks, reveal=True)


card = ItemCardDef(
    guid="621b05a3-ec94-5aaf-ba07-099dfe7b2b54",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyRescue.Name",
    display_name="Buddy-Buddy Rescue",
    searchable_by=["Buddy-Buddy Rescue", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=buddy_buddy_rescue
)
