from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import super_potion, super_potion_condition


card = ItemCardDef(
    guid="f7d475d4-7947-5aa8-b375-59f37a015e42",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion"],
    subtypes=[],
    collector_number=117,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    condition=super_potion_condition,
    effect=super_potion,
)
