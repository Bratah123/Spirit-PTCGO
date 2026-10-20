from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f827aa15-b0c6-58a2-8fcb-21f1ccff73ac",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=137,
    set_code="BW7",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
