from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import has_cards_in_deck, poke_ball


card = ItemCardDef(
    guid="ea0157c8-db2a-5fe7-b8a7-246b6f96f09d",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball"],
    subtypes=[],
    collector_number=121,
    set_code="BASE4",
    rarity=Rarities.Common,
    condition=has_cards_in_deck,
    effect=poke_ball,
)
