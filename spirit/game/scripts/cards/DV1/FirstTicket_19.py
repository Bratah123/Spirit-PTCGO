from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b8b699ef-ee96-5095-9f64-d356f12f6016",
    key="DV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FirstTicket.Name",
    display_name="First Ticket",
    searchable_by=["First Ticket", "Item"],
    subtypes=["Item"],
    collector_number=19,
    set_code="DV1",
    rarity=Rarities.Common,
    effect=unimplemented
)
