"""EX13 Holon Phantoms — Holon Fossil.
"""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import holon_fossil_item


card = ItemCardDef(
    guid="1a2d4b1c-8a4d-579a-971b-501df98c89dd",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonFossil.Name",
    display_name="Holon Fossil",
    searchable_by=["Holon Fossil", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    effect=holon_fossil_item(),
)
