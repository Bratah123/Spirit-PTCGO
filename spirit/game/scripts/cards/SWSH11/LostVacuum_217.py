from spirit.game.card_effects.trainers import lost_vacuum, lost_vacuum_playable
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="34d33698-c1bc-5ab8-937b-e80f6027a461",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostVacuum.Name",
    display_name="Lost Vacuum",
    searchable_by=["Lost Vacuum", "Item"],
    subtypes=["Item"],
    collector_number=217,
    set_code="SWSH11",
    rarity=Rarities.RareSecret,
    effect=lost_vacuum,
    condition=lost_vacuum_playable
)
