from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty


def _is_colorless_pokemon(card):
    return is_pokemon_card(card) and PokemonTypes.COLORLESS.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = SupporterCardDef(
    guid="df800b75-141c-52e4-bfb7-039b578a4057",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Winona.Name",
    display_name="Winona",
    searchable_by=["Winona", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="XY6",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(_is_colorless_pokemon, count=3, minimum=0, reveal=True,
                           prompt='Choose up to 3 Colorless Pokémon'),
    condition=deck_nonempty
)
