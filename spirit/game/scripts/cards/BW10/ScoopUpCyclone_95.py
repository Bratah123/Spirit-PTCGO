from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ef31f3c0-8c03-5904-9a30-af0472e7a8d2",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUpCyclone.Name",
    display_name="Scoop Up Cyclone",
    searchable_by=["Scoop Up Cyclone", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=95,
    set_code="BW10",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
