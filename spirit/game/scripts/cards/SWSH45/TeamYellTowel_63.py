from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.session.passives import effective_max_hp


def _is_damaged(board, pokemon):
    return pokemon is not None and \
        pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def _team_yell_towel_condition(board, player_id):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    mine = board.active_pokemon(player_id)
    theirs = board.active_pokemon(opponent) if opponent else None
    return _is_damaged(board, mine) or _is_damaged(board, theirs)


async def team_yell_towel(ctx):
    """Heal 50 damage from both Active Pokemon."""
    my_active = ctx.my_active()
    if my_active is not None:
        await ctx.heal(50, target=my_active)
    opponent_active = ctx.opponent_active()
    if opponent_active is not None:
        await ctx.heal(50, target=opponent_active)


card = ItemCardDef(
    guid="979176fc-395b-5e8e-8439-68786787763b",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamYellTowel.Name",
    display_name="Team Yell Towel",
    searchable_by=["Team Yell Towel", "Item"],
    subtypes=["Item"],
    collector_number=63,
    set_code="SWSH45",
    rarity=Rarities.Uncommon,
    effect=team_yell_towel,
    condition=_team_yell_towel_condition,
)
