from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, PokemonTypes, AttrID
from spirit.game.session.effects import is_evolution_pokemon


def _is_evolution_grass(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_evolution_pokemon(card) and PokemonTypes.GRASS.value in types


async def turffield_stadium(ctx):
    """Once during each player's turn, that player may search their deck for
    an Evolution Grass Pokemon, reveal it, and put it into their hand."""
    picks = await ctx.search_deck(
        _is_evolution_grass, count=1, minimum=0,
        prompt="Choose an Evolution Grass Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


TURFFIELD_STADIUM_ABILITY = Ability(
    title="Turffield Stadium",
    game_text="Once during each player's turn, that player may search their deck for an Evolution Grass Pokémon, reveal it, and put it into their hand. Then, that player shuffles their deck.",
    activation=Activations.ONCE_PER_TURN,
    effect=turffield_stadium,
)

card = StadiumCardDef(
    guid="645a53c8-3e64-58c3-8d2b-9f451b815cf0",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TurffieldStadium.Name",
    display_name="Turffield Stadium",
    searchable_by=["Turffield Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=68,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    ability=TURFFIELD_STADIUM_ABILITY,
)
