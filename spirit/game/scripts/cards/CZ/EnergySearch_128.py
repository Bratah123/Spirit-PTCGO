from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="bf6f6925-4dec-564b-9e28-1f7eb5c72876",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="CZ",
    rarity=Rarities.Common,
    effect=unimplemented
)
