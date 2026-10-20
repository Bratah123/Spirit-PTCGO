from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


card = SupporterCardDef(
    guid="215733d5-9be6-58bd-a058-252d1a91c14f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Trevor.Name",
    display_name="Trevor",
    searchable_by=["Trevor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=33,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=search_to_hand(is_pokemon_card, count=1, minimum=0, reveal=True, prompt="Choose a Pokémon")
)
