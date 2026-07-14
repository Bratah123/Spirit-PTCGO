from spirit.game.data_utils import SupporterCardDef, is_pokemon_v
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import (
    attach_from_discard, requires_discard, requires_in_play,
)


def _is_water_energy(card):
    return energy_provides_type(card, PokemonTypes.WATER.value)


def _is_v_pokemon(pokemon):
    return is_pokemon_v(pokemon.archetype_id)


def _melony_condition(board, player_id):
    return (
        requires_discard(_is_water_energy)(board, player_id)
        and requires_in_play(_is_v_pokemon, side="mine")(board, player_id)
    )


async def _melony_draw(ctx, picks):
    await ctx.draw_cards(3)


melony = attach_from_discard(
    predicate=_is_water_energy, target=_is_v_pokemon, then=_melony_draw,
    prompt="Choose a Water Energy card to attach.",
)

card = SupporterCardDef(
    guid="b7b8484f-fdcf-5889-8798-7a8dc353f64e",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Melony.Name",
    display_name="Melony",
    searchable_by=["Melony", "Supporter"],
    subtypes=["Supporter"],
    collector_number=218,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    effect=melony,
    condition=_melony_condition,
)
