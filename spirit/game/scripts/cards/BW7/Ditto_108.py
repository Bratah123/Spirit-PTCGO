from spirit.game.data_utils import PokemonCardDef, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.effects import is_basic_pokemon


def _transform_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return any(is_basic_pokemon(c) for c in (hand.children if hand else []))


async def _transform(ctx):
    """Put a Basic Pokemon from your hand on top of this Pokemon; it becomes
    that Pokemon, keeping attachments, damage, Special Conditions, turns in
    play and effects. Ditto stays underneath the new Pokemon and leaves play
    with it."""
    pool = [c for c in ctx.hand() if is_basic_pokemon(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Choose a Basic Pok\u00e9mon to transform into")
    if picks:
        await ctx.identity_swap(ctx.source, picks[0], destination="underneath", transfer=True)


card = PokemonCardDef(
    guid="3e6a15d9-4cdf-5450-9675-f9c2ee05b8a2",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Transform",
            game_text="During your turn (before your attack), you may put a Basic Pok\u00e9mon from your hand on top of this Pok\u00e9mon. (This does not count as playing that Pok\u00e9mon or evolving.) This Pok\u00e9mon is now that Pok\u00e9mon. (Any cards attached to this Pok\u00e9mon, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.UNLIMITED,
            condition=_transform_condition,
            effect=_transform,
        ),
    ],
)