from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b5f85814-dbe1-5495-bcda-cdee9d7f4442",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DowsingMachine.Name",
    display_name="Dowsing Machine",
    searchable_by=["Dowsing Machine", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=128,
    set_code="BW8",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
