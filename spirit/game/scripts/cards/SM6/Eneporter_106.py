from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import eneporter, eneporter_condition

card = ItemCardDef(
    guid="e4d8a65f-5efa-58de-97f0-f0528cbe0716",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eneporter.Name",
    display_name="Eneporter",
    searchable_by=["Eneporter", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    condition=eneporter_condition,
    effect=eneporter,
)
