from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_water_energy_card
from spirit.game.session.effects import is_water_pokemon


def _benched_water(pokemon):
    return is_water_pokemon(pokemon) and not is_in_active_spot(pokemon)


def aqua_patch_playable(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    if not discard or not any(is_water_energy_card(c) for c in discard.children):
        return False
    return any(_benched_water(p) for p in board.pokemon_in_play(player_id))


card = ItemCardDef(
    guid="073d26a6-da8c-5445-ab3c-897f46bc25a2",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AquaPatch.Name",
    display_name="Aqua Patch",
    searchable_by=["Aqua Patch", "Item"],
    subtypes=["Item"],
    collector_number=119,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=aqua_patch_playable,
    effect=attach_from_discard(
        is_water_energy_card, count=1, target=_benched_water,
        prompt="Choose a Water Energy card to attach.",
    ),
)
