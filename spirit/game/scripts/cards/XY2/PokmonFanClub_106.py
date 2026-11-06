from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="f24d926d-83b8-5432-9ddd-0eb92c281771",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonFanClub.Name",
    display_name="Pok\u00e9mon Fan Club",
    searchable_by=["Pokémon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=106,
    set_code="XY2",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_basic_pokemon, count=2, minimum=0, reveal=True,
                           prompt='Choose up to 2 Basic Pokémon'),
    condition=deck_nonempty
)
