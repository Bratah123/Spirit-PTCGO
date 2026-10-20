from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="56651494-fb94-5b38-9de7-64e8845b5336",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HypnotoxicLaser.Name",
    display_name="Hypnotoxic Laser",
    searchable_by=["Hypnotoxic Laser", "Item", "Team Plasma"],
    subtypes=["Item", "Team Plasma"],
    collector_number=123,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
