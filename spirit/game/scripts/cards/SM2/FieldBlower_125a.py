from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.scripts.cards.SM2.FieldBlower_125 import field_blower, field_blower_playable

card = ItemCardDef(
    guid="bfaa43c6-8b9a-5b7d-bc98-34bfb2adf7f7",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieldBlower.Name",
    display_name="Field Blower",
    searchable_by=["Field Blower", "Item"],
    subtypes=["Item"],
    collector_number=177,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=field_blower_playable,
    effect=field_blower,
)
