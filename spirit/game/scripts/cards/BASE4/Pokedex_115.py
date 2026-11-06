from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import has_cards_in_deck, pokedex


card = ItemCardDef(
    guid="b8ddbc72-9ceb-5ecd-bc47-9869b769a3e1",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokedex.Name",
    display_name="Pokédex",
    searchable_by=["Pok\u00e9dex"],
    subtypes=[],
    collector_number=115,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    condition=has_cards_in_deck,
    effect=pokedex,
)
