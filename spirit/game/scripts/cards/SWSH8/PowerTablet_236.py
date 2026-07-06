from spirit.game.card_effects.trainers import power_tablet
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b956c045-014f-5a91-ad12-81fbbd7a52b7",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerTablet.Name",
    display_name="Power Tablet",
    searchable_by=["Power Tablet", "Item", "Fusion Strike"],
    subtypes=["Item", "Fusion Strike"],
    collector_number=236,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=power_tablet
)
