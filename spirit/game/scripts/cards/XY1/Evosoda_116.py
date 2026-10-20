from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import evolution_blocked


def _evolvable(board, turn_state, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if not evolution_blocked(board, player_id, p)
            and (turn_state is None or turn_state.may_evolve_target(p.entity_id))]


def evosoda_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and bool(board.pokemon_in_play(player_id))


async def evosoda(ctx):
    """Search your deck for a card that evolves from 1 of your Pokemon and put
    it onto that Pokemon (counts as evolving); shuffle. Not during your first
    turn or onto a Pokemon put into play this turn."""
    targets = _evolvable(ctx.board, ctx.session.turn_state, ctx.player_id)
    names = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) for p in targets}

    def _fits(card):
        return is_pokemon_card(card) and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) in names

    picks = await ctx.search_deck(_fits, count=1, minimum=0, prompt="Choose a card to evolve into")
    if picks:
        evo = picks[0]
        pool = [p for p in targets if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
                == evo.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)]
        target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Choose a Pokémon to evolve")
        if pool:
            await ctx.evolve_pokemon(target or pool[0], evo)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="180b57c2-e73c-5589-86fb-7242717055e6",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evosoda.Name",
    display_name="Evosoda",
    searchable_by=["Evosoda", "Item"],
    subtypes=["Item"],
    collector_number=116,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=evosoda,
    condition=evosoda_condition
)
