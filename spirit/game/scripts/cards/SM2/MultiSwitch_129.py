from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_energy_card, player_has_bench


def multi_switch_playable(board, player_id):
    if not player_has_bench(board, player_id):
        return False
    bench = board.find_player_area(player_id, "bench")
    if bench is None:
        return False
    return any(any(is_energy_card(c) for c in p.children) for p in bench.children)


async def multi_switch(ctx):
    """Move an Energy from 1 of your Benched Pokémon to your Active Pokémon."""
    active = ctx.my_active()
    if active is None:
        return
    await ctx.move_energy_freely(ctx.my_bench(), [active], max_count=1)


card = ItemCardDef(
    guid="0c698d08-3e32-57c7-b9ef-f490af9b53e7",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiSwitch.Name",
    display_name="Multi Switch",
    searchable_by=["Multi Switch", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=multi_switch_playable,
    effect=multi_switch,
)
