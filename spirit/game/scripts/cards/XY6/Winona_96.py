from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty


def _is_colorless_pokemon(card):
    return is_pokemon_card(card) and PokemonTypes.COLORLESS.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = SupporterCardDef(
    guid="2d508c1f-20bd-592d-a839-2043f63b4385",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Winona.Name",
    display_name="Winona",
    searchable_by=["Winona", "Supporter"],
    subtypes=["Supporter"],
    collector_number=96,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(_is_colorless_pokemon, count=3, minimum=0, reveal=True,
                           prompt='Choose up to 3 Colorless Pokémon'),
    condition=deck_nonempty
)
