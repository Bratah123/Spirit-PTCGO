from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AttrID
from spirit.game.session.passives import effective_max_hp


def _in_play(board, player_id):
    active = board.find_player_area(player_id, "activePokemonArea")
    bench = board.find_player_area(player_id, "bench")
    return [p for area in (active, bench) if area for p in area.children]


def _festival_condition(board, player_id, stadium=None):
    mine = _in_play(board, player_id)
    return len(mine) == 6 and any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p) for p in mine)


async def champions_festival(ctx):
    """If you have 6 Pokemon in play, heal 10 damage from each of your Pokemon."""
    mine = ctx.my_pokemon_in_play()
    if len(mine) != 6:
        return
    for pokemon in mine:
        await ctx.heal(10, pokemon)


CHAMPIONS_FESTIVAL_ABILITY = Ability(
    title="Champions Festival",
    game_text="Once during each player's turn, if that player has 6 Pok\u00e9mon in play, he or she may heal 10 damage from each of his or her Pok\u00e9mon.",
    activation=Activations.ONCE_PER_TURN,
    condition=_festival_condition,
    effect=champions_festival,
)


card = StadiumCardDef(
    guid="83751a88-bd2d-5f9f-b52f-baba3ce577f1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    ability=CHAMPIONS_FESTIVAL_ABILITY
)
