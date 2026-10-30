from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import has_cards_in_deck, new_pokedex


card = ItemCardDef(
    guid="a6380331-b72d-51d8-9539-ff06e088b34a",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NewPokedex.Name",
    display_name="New Pokédex",
    searchable_by=["New Pok\u00e9dex"],
    subtypes=[],
    collector_number=95,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    condition=has_cards_in_deck,
    effect=new_pokedex,
)
