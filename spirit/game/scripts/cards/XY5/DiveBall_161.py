from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty


def _is_water_pokemon(card):
    return is_pokemon_card(card) and PokemonTypes.WATER.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = ItemCardDef(
    guid="6adcfc8e-7875-5de9-b36d-8f7b2ea10fb6",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DiveBall.Name",
    display_name="Dive Ball",
    searchable_by=["Dive Ball", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="XY5",
    rarity=Rarities.RareSecret,
    effect=search_to_hand(_is_water_pokemon, count=1, minimum=0, reveal=True,
                           prompt='Choose a Water Pokémon'),
    condition=deck_nonempty
)
