from spirit.game.card_effects.trainers import ordinary_rod
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8ac64122-d101-55bf-a9a3-5841949d0f0e",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OrdinaryRod.Name",
    display_name="Ordinary Rod",
    searchable_by=["Ordinary Rod", "Item"],
    subtypes=["Item"],
    collector_number=215,
    set_code="SWSH1",
    rarity=Rarities.RareSecret,
    effect=ordinary_rod
)
