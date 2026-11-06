from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.models.board import PokemonEntity
from spirit.game.card_effects.pokemon import devolvable


def _my_evolved(board, player_id):
    return [p for p in board.pokemon_in_play(player_id) if devolvable(p)]


def _devolution_spray_condition(board, player_id, card=None):
    return bool(_my_evolved(board, player_id))


async def devolution_spray(ctx):
    """Devolve 1 of your evolved Pok\u00e9mon; the highest Stage card goes to
    your hand and the remaining Pok\u00e9mon can't evolve this turn."""
    candidates = _my_evolved(ctx.board, ctx.player_id)
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose 1 of your evolved Pok\u00e9mon to devolve")
    if target is None:
        return
    evolves_from = target.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
    below = next((c for c in target.children if isinstance(c, PokemonEntity)
                  and c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == evolves_from), None)
    await ctx.devolve_pokemon(target, steps=1, destination="hand")
    if below is not None:
        ctx.session.turn_state.mark_entered_play(below.entity_id)


card = ItemCardDef(
    guid="596eb03a-6cff-5ba6-8a9e-e3fb245b2630",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSpray.Name",
    display_name="Devolution Spray",
    searchable_by=["Devolution Spray", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=devolution_spray,
    condition=_devolution_spray_condition
)
