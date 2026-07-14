from spirit.game.card_effects.trainers import lost_vacuum, lost_vacuum_playable
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="de9e562a-61d8-59e7-af6e-af8f1b72b86d",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostVacuum.Name",
    display_name="Lost Vacuum",
    searchable_by=["Lost Vacuum", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=lost_vacuum,
    condition=lost_vacuum_playable
)
