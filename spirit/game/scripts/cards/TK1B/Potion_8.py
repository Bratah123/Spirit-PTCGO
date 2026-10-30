from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="b99f85cc-2524-54ed-bcea-11dd3f7dd5cb",
    key="TK1B",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=8,
    set_code="TK1B",
    rarity=Rarities.Common,
    condition=requires_damaged_pokemon(),
    effect=heal_item(30)
)
