from spirit.game.data_utils import SupporterCardDef, is_pokemon_v
from spirit.game.attributes import Rarities
from spirit.game.models.board import PokemonEntity
from spirit.game.session.effects import full_stack


def _volo_condition(board, player_id):
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(
        isinstance(c, PokemonEntity) and is_pokemon_v(c.archetype_id)
        for c in bench.children
    )


async def volo(ctx):
    """Discard 1 of your Benched Pokemon V and all attached cards."""
    candidates = [p for p in ctx.my_bench() if is_pokemon_v(p.archetype_id)]
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your Benched Pokémon V to discard"
    )
    if target is None:
        return
    await ctx.discard_cards(full_stack(target))


card = SupporterCardDef(
    guid="81375ea6-9130-55f6-b90f-d3fdcde878e0",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Volo.Name",
    display_name="Volo",
    searchable_by=["Volo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=169,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    condition=_volo_condition,
    effect=volo,
)
