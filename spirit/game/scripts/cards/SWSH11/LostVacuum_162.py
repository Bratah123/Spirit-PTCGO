from spirit.game.card_effects.trainers import lost_vacuum, lost_vacuum_playable
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="60a35514-a1e0-5c3a-9ff0-1fe1dd718e18",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostVacuum.Name",
    display_name="Lost Vacuum",
    searchable_by=["Lost Vacuum", "Item"],
    subtypes=["Item"],
    collector_number=162,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    effect=lost_vacuum,
    condition=lost_vacuum_playable
)
