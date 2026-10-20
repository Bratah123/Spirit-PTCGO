from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c44dca6a-27da-56f3-89bc-3e49607496ea",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=94,
    set_code="BW10",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
