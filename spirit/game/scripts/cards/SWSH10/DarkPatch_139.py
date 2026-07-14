from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, PokemonTypes, AttrID
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot


def _is_basic_darkness_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.DARKNESS.value in types


def _is_benched_darkness_pokemon(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return not is_in_active_spot(pokemon) and PokemonTypes.DARKNESS.value in types


def _dark_patch_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    bench_children = bench.children if bench else []
    if not any(PokemonTypes.DARKNESS.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])
               for p in bench_children):
        return False
    discard = board.find_player_area(player_id, "discard")
    cards = discard.children if discard else []
    return any(_is_basic_darkness_energy(c) for c in cards)


card = ItemCardDef(
    guid="f3804cce-d01c-5887-bca9-6408572e8f32",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkPatch.Name",
    display_name="Dark Patch",
    searchable_by=["Dark Patch", "Item"],
    subtypes=["Item"],
    collector_number=139,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(
        predicate=_is_basic_darkness_energy, count=1, minimum=1,
        target=_is_benched_darkness_pokemon,
        prompt="Choose a basic Darkness Energy card to attach to a Benched Darkness Pokémon",
    ),
    condition=_dark_patch_condition
)
