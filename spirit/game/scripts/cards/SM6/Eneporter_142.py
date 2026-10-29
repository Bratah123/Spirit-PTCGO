from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import eneporter, eneporter_condition

card = ItemCardDef(
    guid="3cedc8b5-8c92-59a5-95f4-94853e06f4ed",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eneporter.Name",
    display_name="Eneporter",
    searchable_by=["Eneporter", "Item"],
    subtypes=["Item"],
    collector_number=142,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    condition=eneporter_condition,
    effect=eneporter,
)
