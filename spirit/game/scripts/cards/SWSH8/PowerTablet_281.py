from spirit.game.card_effects.trainers import power_tablet
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7555a278-2bdb-593b-979e-de8692e39e3f",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerTablet.Name",
    display_name="Power Tablet",
    searchable_by=["Power Tablet", "Item", "Fusion Strike"],
    subtypes=["Item", "Fusion Strike"],
    collector_number=281,
    set_code="SWSH8",
    rarity=Rarities.RareSecret,
    effect=power_tablet
)
