from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def _my_energies(board, player_id):
    return [e for p in board.pokemon_in_play(player_id) for e in board.attached_energies(p)]


def energy_reset_condition(board, player_id):
    return bool(_my_energies(board, player_id))


async def energy_reset(ctx):
    """Put as many Energy attached to your Pokemon as you like into your hand."""
    pool = _my_energies(ctx.board, ctx.player_id)
    picked = await ctx.choose_cards(pool, len(pool), minimum=0,
                                    prompt="Choose any Energy to put into your hand")
    if picked:
        await ctx.put_in_hand(picked, reveal=False)


card = ItemCardDef(
    guid="5519f2fa-f23f-5eb2-93b0-9d5d836802de",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyReset.Name",
    display_name="Energy Reset",
    searchable_by=["Energy Reset", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    condition=energy_reset_condition,
    effect=energy_reset
)
