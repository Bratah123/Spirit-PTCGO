from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.content.definitions import def_for


async def _scout(ctx):
    """Your opponent reveals their hand."""
    await ctx.reveal_hand(ctx.opponent_id)


def _named(card, *names):
    d = def_for(card.archetype_id)
    return getattr(d, "display_name", None) in names


def _is_stadium(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


def _teleport_condition(board, player_id, pokemon=None):
    area = board.find_global_area("activeStadium")
    current = area.children[0] if area and area.children else None
    discard = board.find_player_area(player_id, "discard")
    if current is None or not discard:
        return False
    name = getattr(def_for(current.archetype_id), "display_name", None)
    return any(_is_stadium(c) and not _named(c, name) for c in discard.children)


async def _teleport_room(ctx):
    """Discard the Stadium in play; if you do, put a Stadium with a different
    name from your discard pile into play."""
    current = ctx.stadium_in_play()
    if current is None:
        return
    name = getattr(def_for(current.archetype_id), "display_name", None)
    if await ctx.discard_stadium() is None:
        return
    cards = [c for c in ctx.discard_pile() if _is_stadium(c) and not _named(c, name)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Stadium to put into play")
    if not picks:
        return
    await ctx.flush_choreography()
    ts = ctx.session.turn_state
    played = ts.stadium_played
    await ctx.session._execute_play_stadium(ctx.player_id, picks[0])
    ts.stadium_played = played  # not "played from hand"


card = PokemonCardDef(
    guid="9eb1697f-42bb-58a6-9a40-68fe2daa79ff",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2", "Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=41,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Ability(
            title="Teleport Room",
            game_text="Once during your turn (before your attack), you may discard any Stadium card in play. If you do, put a Stadium card with a different name from your discard pile into play.",
            activation=Activations.ONCE_PER_TURN,
            condition=_teleport_condition,
            effect=_teleport_room,
        ),
        Attack(
            title="Psy Report",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_scout,
        ),
    ],
)