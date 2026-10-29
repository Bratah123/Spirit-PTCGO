from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import fossil_excavation_map, fossil_excavation_map_condition

card = ItemCardDef(
    guid="6b7d0bfc-a78a-5fd6-9d2d-bf502534705e",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavationMap.Name",
    display_name="Fossil Excavation Map",
    searchable_by=["Fossil Excavation Map", "Item"],
    subtypes=["Item"],
    collector_number=107,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    condition=fossil_excavation_map_condition,
    effect=fossil_excavation_map,
)
