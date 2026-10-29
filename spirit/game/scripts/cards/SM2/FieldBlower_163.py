from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.scripts.cards.SM2.FieldBlower_125 import field_blower, field_blower_playable

card = ItemCardDef(
    guid="872fae20-13e1-5379-a9e1-e929439f68e4",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieldBlower.Name",
    display_name="Field Blower",
    searchable_by=["Field Blower", "Item"],
    subtypes=["Item"],
    collector_number=163,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    condition=field_blower_playable,
    effect=field_blower,
)
