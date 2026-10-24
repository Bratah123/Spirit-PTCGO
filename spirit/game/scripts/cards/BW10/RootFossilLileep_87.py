from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import restore_fossil

card = ItemCardDef(
    guid="972135c9-19af-57e4-8f29-3c663fcfd9d0",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossilLileep.Name",
    display_name="Root Fossil Lileep",
    searchable_by=["Root Fossil Lileep", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=restore_fossil("Lileep")
)
