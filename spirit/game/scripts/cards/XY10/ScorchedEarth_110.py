from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _fire_or_fighting(card):
    return is_energy_card(card) and (energy_provides_type(card, PokemonTypes.FIRE.value)
                                     or energy_provides_type(card, PokemonTypes.FIGHTING.value))


def scorched_earth_condition(board, player_id, stadium=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_fire_or_fighting(c) for c in hand.children)


async def scorched_earth(ctx):
    """Discard a Fire or Fighting Energy card from your hand; if you do, draw 2."""
    picked = await ctx.discard_from_hand(1, minimum=1, predicate=_fire_or_fighting,
                                         prompt="Discard a Fire or Fighting Energy card")
    if picked:
        await ctx.draw_cards(2)


card = StadiumCardDef(
    guid="f7889519-a4be-59dc-9f00-5dc4bfac83af",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScorchedEarth.Name",
    display_name="Scorched Earth",
    searchable_by=["Scorched Earth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=110,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Scorched Earth",
        game_text="Once during each player's turn, that player may discard a Fire or Fighting Energy card from his or her hand. If that player does so, he or she draws 2 cards.",
        activation=Activations.ONCE_PER_TURN,
        effect=scorched_earth,
        condition=scorched_earth_condition,
    )
)
