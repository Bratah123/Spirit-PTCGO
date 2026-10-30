from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import has_cards_in_deck, poke_ball


card = ItemCardDef(
    guid="4b0489f7-d7e0-5b1c-a27b-a73dc98e6867",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball"],
    subtypes=[],
    collector_number=64,
    set_code="BASE2",
    rarity=Rarities.Common,
    condition=has_cards_in_deck,
    effect=poke_ball,
)
