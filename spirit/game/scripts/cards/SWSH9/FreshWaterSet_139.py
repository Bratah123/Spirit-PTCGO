from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="84fa460d-a5b0-555b-bb3f-08a04e4d173b",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FreshWaterSet.Name",
    display_name="Fresh Water Set",
    searchable_by=["Fresh Water Set", "Item"],
    subtypes=["Item"],
    collector_number=139,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    effect=heal_item(20, scope="each_own"),
    condition=requires_damaged_pokemon()
)
