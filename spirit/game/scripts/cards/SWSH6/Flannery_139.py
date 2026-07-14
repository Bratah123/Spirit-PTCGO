from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_special_energy


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def _opponent_special_energies(board, player_id):
    opponent = _other_player(board, player_id)
    if not opponent:
        return []
    out = []
    for pokemon in board.pokemon_in_play(opponent):
        out.extend(c for c in pokemon.children if is_special_energy(c))
    return out


def _flannery_condition(board, player_id):
    if _opponent_special_energies(board, player_id):
        return True
    stadium_area = board.find_global_area("activeStadium")
    return bool(stadium_area and stadium_area.children)


async def flannery(ctx):
    """Discard a Special Energy from 1 of your opponent's Pokemon, and
    discard a Stadium in play."""
    targets = _opponent_special_energies(ctx.board, ctx.player_id)
    if targets:
        picks = await ctx.choose_cards(
            targets, 1, minimum=1, prompt="Choose a Special Energy to discard"
        )
        await ctx.discard_cards(picks)
    await ctx.discard_stadium()


card = SupporterCardDef(
    guid="aea34f9a-0064-5d11-9613-e1bd7455c2e1",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Flannery.Name",
    display_name="Flannery",
    searchable_by=["Flannery", "Supporter", "Single Strike"],
    subtypes=["Supporter", "Single Strike"],
    collector_number=139,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    effect=flannery,
    condition=_flannery_condition,
)
