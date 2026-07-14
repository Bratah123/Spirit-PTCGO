from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="0673acf4-d7f4-52c1-87cd-67e9eda9f4e1",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=139,
    set_code="CZ",
    rarity=Rarities.Common,
    condition=requires_damaged_pokemon(),
    effect=heal_item(30)
)
