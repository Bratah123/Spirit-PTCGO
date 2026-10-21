from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import evolution_blocked
from spirit.game.card_effects.attacks_common import condition_attack


def _is_confused(pokemon):
    conds = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    return CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.CONFUSED] in conds


def _upside_down_condition(board, player_id, pokemon=None):
    deck = board.find_player_area(player_id, "deck")
    return (pokemon is not None and _is_confused(pokemon) and bool(deck and deck.children)
            and not evolution_blocked(board, player_id, pokemon))


async def _upside_down_evolution(ctx):
    """If this Pokemon is Confused, search your deck for a card that evolves
    from it and put it onto it (counts as evolving); shuffle."""
    me = ctx.source
    name = me.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

    def _fits(card):
        return is_pokemon_card(card) and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name

    picks = await ctx.search_deck(_fits, count=1, minimum=0, prompt="Choose a card that evolves from this Pokémon")
    if picks:
        await ctx.evolve_pokemon(me, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ed0be64c-c5c0-58ef-8f90-847e563c0c78",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic", "Inkay"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=686,
    abilities=[
        Ability(
            title="Upside-Down Evolution",
            game_text="Once during your turn, (before your attack), if this Pok\u00e9mon is Confused, you may search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon. (This counts as evolving this Pok\u00e9mon.) Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            condition=_upside_down_condition,
            effect=_upside_down_evolution,
        ),
        Attack(
            title="Confusion Wave",
            game_text="Both Active Pok\u00e9mon are now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, both_actives=True),
        ),
    ],
)