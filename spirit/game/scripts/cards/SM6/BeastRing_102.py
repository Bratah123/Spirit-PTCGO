from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import beast_ring, beast_ring_condition

card = ItemCardDef(
    guid="a5a09892-5089-5bc2-a07f-6aa5ec14e659",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastRing.Name",
    display_name="Beast Ring",
    searchable_by=["Beast Ring", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="SM6",
    rarity=Rarities.Rare,
    condition=beast_ring_condition,
    effect=beast_ring,
)
