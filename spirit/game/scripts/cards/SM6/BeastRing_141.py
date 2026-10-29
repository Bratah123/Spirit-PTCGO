from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import beast_ring, beast_ring_condition

card = ItemCardDef(
    guid="b74c928f-bf67-5d3d-9059-e00ffe40b7e3",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastRing.Name",
    display_name="Beast Ring",
    searchable_by=["Beast Ring", "Item"],
    subtypes=["Item"],
    collector_number=141,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    condition=beast_ring_condition,
    effect=beast_ring,
)
