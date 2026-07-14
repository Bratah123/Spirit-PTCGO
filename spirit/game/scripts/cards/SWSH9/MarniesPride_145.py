from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


def _marnies_pride_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    has_energy = bool(discard) and any(is_basic_energy_card(c) for c in discard.children)
    bench = board.find_player_area(player_id, "bench")
    has_bench = bool(bench) and bool(bench.children)
    return has_energy and has_bench


async def marnies_pride(ctx):
    """Attach a basic Energy card from your discard pile to 1 of your
    Benched Pokemon."""
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    bench = ctx.my_bench()
    if not energy or not bench:
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=1,
        prompt="Choose a basic Energy card to attach.",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = SupporterCardDef(
    guid="59bf1106-1947-5649-a535-e9505ad024e6",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MarniesPride.Name",
    display_name="Marnie's Pride",
    searchable_by=["Marnie's Pride", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    effect=marnies_pride,
    condition=_marnies_pride_condition,
)
