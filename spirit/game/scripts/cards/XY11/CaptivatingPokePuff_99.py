from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon


async def captivating_poke_puff(ctx):
    """Your opponent reveals their hand; put any number of Basic Pokemon found
    there onto their Bench."""
    await ctx.reveal_hand(ctx.opponent_id)
    pool = [c for c in ctx.hand(ctx.opponent_id) if is_basic_pokemon(c)]
    if not pool:
        return
    picked = await ctx.choose_cards(pool, len(pool), minimum=0,
                                    prompt="Put any Basic Pokémon onto your opponent's Bench")
    for c in picked:
        if not await ctx.bench_pokemon(c):
            break


card = ItemCardDef(
    guid="7ca0fb60-d5de-56ff-81e8-3553f6412d94",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CaptivatingPokePuff.Name",
    display_name="Captivating Pok\u00e9 Puff",
    searchable_by=["Captivating Poké Puff", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    effect=captivating_poke_puff
)
