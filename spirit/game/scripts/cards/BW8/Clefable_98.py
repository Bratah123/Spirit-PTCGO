from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.session.passives import evolution_blocked
from spirit.game.session.effects import is_pokemon_card


def _evolvable(board, session_state, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if not evolution_blocked(board, player_id, p)
            and (session_state is None or session_state.may_evolve_target(p.entity_id))]


def _moon_condition(board, player_id, pokemon=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and bool(board.pokemon_in_play(player_id))


async def _moon_guidance(ctx):
    """Flip a coin. If heads, search your deck for a card that evolves from 1
    of your Pokemon and put it onto that Pokemon (counts as evolving); shuffle."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not results or not results[0]:
        return
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
        if target is not None or pool:
            await ctx.evolve_pokemon(target or pool[0], evo)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="a20bf86c-5341-5553-acb8-883c552eeda3",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Ability(
            title="Moon Guidance",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a card that evolves from 1 of your Pok\u00e9mon and put it onto that Pok\u00e9mon. (This counts as evolving that Pok\u00e9mon.) Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_moon_condition,
            effect=_moon_guidance,
        ),
        Attack(
            title="Moon Impact",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)