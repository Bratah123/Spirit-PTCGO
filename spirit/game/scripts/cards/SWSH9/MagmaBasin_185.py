from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.card_effects.pokemon import energy_provides_type


def _is_fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


def _is_fire_pokemon(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value in types


def _magma_basin_condition(board, player_id, stadium):
    discard = board.find_player_area(player_id, "discard")
    has_energy = bool(discard) and any(_is_fire_energy(c) for c in discard.children)
    bench = board.find_player_area(player_id, "bench")
    has_bench = bool(bench) and any(_is_fire_pokemon(p) for p in bench.children)
    return has_energy and has_bench


async def _magma_basin_effect(ctx):
    """Once during each player's turn, that player may attach a Fire Energy from
    their discard pile to 1 of their Benched Fire Pokemon and put 2 damage
    counters on it."""
    energy = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
    bench = [p for p in ctx.my_bench() if _is_fire_pokemon(p)]
    if not energy or not bench:
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=1,
        prompt="Choose a Fire Energy card to attach.",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Fire Pokémon")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)
    await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)


MAGMA_BASIN_ABILITY = Ability(
    title="Magma Basin",
    game_text="Once during each player's turn, that player may attach a Fire Energy card from their discard pile to 1 of their Benched Fire Pokémon. If a player attached Energy to a Pokémon in this way, put 2 damage counters on that Pokémon.",
    activation=Activations.ONCE_PER_TURN,
    effect=_magma_basin_effect,
    condition=_magma_basin_condition,
)

card = StadiumCardDef(
    guid="f65c94a9-a1f8-53e4-b8ff-3dd1ff150979",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MagmaBasin.Name",
    display_name="Magma Basin",
    searchable_by=["Magma Basin", "Stadium"],
    subtypes=["Stadium"],
    collector_number=185,
    set_code="SWSH9",
    rarity=Rarities.RareSecret,
    ability=MAGMA_BASIN_ABILITY,
)
