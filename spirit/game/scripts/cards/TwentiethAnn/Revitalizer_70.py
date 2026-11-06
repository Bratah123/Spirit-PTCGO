from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, PokemonTypes, AttrID
from spirit.game.session.effects import is_pokemon_card


def _pool(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return [c for c in (discard.children if discard else [])
            if is_pokemon_card(c) and PokemonTypes.GRASS.value in (c.get_attribute(AttrID.POKEMON_TYPES) or [])]


def revitalizer_condition(board, player_id):
    return bool(_pool(board, player_id))


async def revitalizer(ctx):
    """Put 2 Grass Pokemon from your discard pile into your hand."""
    pool = _pool(ctx.board, ctx.player_id)
    n = min(2, len(pool))
    picked = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Grass Pokémon")
    if picked:
        await ctx.put_in_hand(picked)


card = ItemCardDef(
    guid="973254e4-58c2-502b-96d2-2ce49008a4bb",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revitalizer.Name",
    display_name="Revitalizer",
    searchable_by=["Revitalizer", "Item"],
    subtypes=["Item"],
    collector_number=70,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    condition=revitalizer_condition,
    effect=revitalizer
)
