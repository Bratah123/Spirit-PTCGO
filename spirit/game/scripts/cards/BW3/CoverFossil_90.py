from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import restore_fossil


card = ItemCardDef(
    guid="f2987372-7898-53bf-810b-e00e3fa45d59",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoverFossil.Name",
    display_name="Cover Fossil",
    searchable_by=["Cover Fossil", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=restore_fossil("Tirtouga"),
)
