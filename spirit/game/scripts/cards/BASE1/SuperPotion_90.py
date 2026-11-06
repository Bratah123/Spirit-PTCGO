from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import super_potion, super_potion_condition


card = ItemCardDef(
    guid="aee1a71a-3df8-5067-b0cb-195ae1ab3724",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion"],
    subtypes=[],
    collector_number=90,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    condition=super_potion_condition,
    effect=super_potion,
)
