from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import has_cards_in_deck, pokedex


card = ItemCardDef(
    guid="32acf046-cf2f-527e-9d42-a512df600cee",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokedex.Name",
    display_name="Pokédex",
    searchable_by=["Pok\u00e9dex"],
    subtypes=[],
    collector_number=87,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    condition=has_cards_in_deck,
    effect=pokedex,
)
