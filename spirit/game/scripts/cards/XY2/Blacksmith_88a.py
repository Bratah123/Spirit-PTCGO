from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _is_fire_pokemon(pokemon):
    return PokemonTypes.FIRE.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def blacksmith_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return (bool(discard) and any(_is_fire_energy_card(c) for c in discard.children)
            and any(_is_fire_pokemon(p) for p in board.pokemon_in_play(player_id)))


async def blacksmith(ctx):
    """Attach 2 Fire Energy cards from your discard pile to 1 of your Fire Pokemon."""
    targets = [p for p in ctx.my_pokemon_in_play() if _is_fire_pokemon(p)]
    cards = [c for c in ctx.discard_pile() if _is_fire_energy_card(c)]
    if not targets or not cards:
        return
    picks = await ctx.choose_cards(cards, 2, prompt="Choose 2 Fire Energy cards")
    if not picks:
        return
    target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
        targets, "Choose a Fire Pokémon to attach them to")
    for card in picks:
        await ctx.attach_energy(card, target or targets[0])


card = SupporterCardDef(
    guid="daa67b30-c096-5261-aa2b-dda00bfb0274",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blacksmith.Name",
    display_name="Blacksmith",
    searchable_by=["Blacksmith", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="XY2",
    rarity=Rarities.RareUltra,
    effect=blacksmith,
    condition=blacksmith_condition
)
