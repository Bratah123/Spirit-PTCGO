from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_metal_energy_card
from spirit.game.session.effects import is_pokemon_card


def _is_metal_pokemon(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.METAL.value in types


def _metal_saucer_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    if not discard or not any(is_metal_energy_card(c) for c in discard.children):
        return False
    return any(_is_metal_pokemon(p) for p in board.pokemon_in_play(player_id)
               if p is not board.active_pokemon(player_id))


async def metal_saucer(ctx):
    """Attach a Metal Energy card from your discard pile to 1 of your
    Benched Metal Pokemon."""
    energies = [c for c in ctx.discard_pile() if is_metal_energy_card(c)]
    if not energies:
        return
    bench = [p for p in ctx.my_bench() if _is_metal_pokemon(p)]
    if not bench:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Metal Energy card to attach"
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Metal Pokémon")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = ItemCardDef(
    guid="7748ae8e-9cb3-54a2-a49f-07bd2e1558da",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalSaucer.Name",
    display_name="Metal Saucer",
    searchable_by=["Metal Saucer", "Item"],
    subtypes=["Item"],
    collector_number=170,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=metal_saucer,
    condition=_metal_saucer_condition,
)
