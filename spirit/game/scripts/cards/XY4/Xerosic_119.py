from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType


def _tool_or_special(card):
    return bool(card.get_attribute(AttrID.IS_SPECIAL_ENERGY)) or card.get_attribute(
        AttrID.TRAINER_TYPE) in (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _pool(board):
    return [c for pid in board.player_ids for p in board.pokemon_in_play(pid)
            for c in p.children if _tool_or_special(c)]


def xerosic_condition(board, player_id):
    return bool(_pool(board))


async def xerosic(ctx):
    """Discard a Pokemon Tool or Special Energy attached to a Pokemon in play."""
    pool = _pool(ctx.board)
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1,
                                   prompt="Choose a Pokémon Tool or Special Energy to discard")
    if picks:
        await ctx.discard_cards(picks)


card = SupporterCardDef(
    guid="d206c0ca-894e-5ece-a6b6-ba5a9761326f",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Xerosic.Name",
    display_name="Xerosic",
    searchable_by=["Xerosic", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    effect=xerosic,
    condition=xerosic_condition
)
