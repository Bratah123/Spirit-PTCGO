from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import has_cards_in_deck, pokemon_name_contains
from spirit.game.card_effects.support_common import search_to_hand


card = ItemCardDef(
    guid="366c7650-ebff-5de4-b32b-80a20bd0600a",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksTrainingMethod.Name",
    display_name="Brock's Training Method",
    searchable_by=["Brock's Training Method"],
    subtypes=[],
    collector_number=106,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    condition=has_cards_in_deck,
    effect=search_to_hand(
        pokemon_name_contains("Brock"),
        prompt="Choose a Basic Pokémon or Evolution card with Brock in its name.",
    ),
)
