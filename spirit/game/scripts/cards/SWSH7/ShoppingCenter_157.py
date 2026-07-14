from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AttrID, TrainerType


def _shopping_center_tools(pokemon_list):
    return [
        child for pokemon in pokemon_list for child in pokemon.children
        if child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
    ]


def shopping_center_condition(board, player_id, stadium):
    return bool(_shopping_center_tools(board.pokemon_in_play(player_id)))


async def shopping_center(ctx):
    """Put a Pokemon Tool attached to 1 of your Pokemon into your hand."""
    tools = _shopping_center_tools(ctx.my_pokemon_in_play())
    if not tools:
        return
    picks = await ctx.choose_cards(
        tools, 1, minimum=1, prompt="Choose a Pokémon Tool to put into your hand."
    )
    await ctx.put_in_hand(picks, reveal=False)


SHOPPING_CENTER_ABILITY = Ability(
    title="Shopping Center",
    game_text="Once during each player's turn, that player may put a Pokémon Tool attached to 1 of their Pokémon into their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=shopping_center,
    condition=shopping_center_condition,
)

card = StadiumCardDef(
    guid="be8c92e0-b5ec-5f00-9c4b-24d7012f3fea",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShoppingCenter.Name",
    display_name="Shopping Center",
    searchable_by=["Shopping Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=157,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    ability=SHOPPING_CENTER_ABILITY,
)
