from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="dc77866f-0d84-527f-af8b-a2e88b40b10f",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="EX14",
    rarity=Rarities.Common,
    condition=requires_damaged_pokemon(),
    effect=heal_item(30)
)
