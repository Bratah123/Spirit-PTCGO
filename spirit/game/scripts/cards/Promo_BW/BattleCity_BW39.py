from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities


def _city_condition(board, player_id, stadium=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def battle_city(ctx):
    """Flip a coin. If heads, draw a card."""
    results = await ctx.flip_coins(1, "Battle City")
    if results and results[0]:
        await ctx.draw_cards(1)


BATTLE_CITY_ABILITY = Ability(
    title="Battle City",
    game_text="Once during each player's turn, that player may flip a coin. If heads, the player draws a card.",
    activation=Activations.ONCE_PER_TURN,
    condition=_city_condition,
    effect=battle_city,
)


card = StadiumCardDef(
    guid="c65bccdc-7c69-57a3-8d15-3faf6864b562",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleCity.Name",
    display_name="Battle City",
    searchable_by=["Battle City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=39,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    ability=BATTLE_CITY_ABILITY
)
