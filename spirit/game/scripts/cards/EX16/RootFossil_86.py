"""EX13 Holon Phantoms — Root Fossil.
"""
from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import ExFossilPassive
from spirit.game.card_effects.trainers import fossil_discard_ability


card = FossilItemCardDef(
    guid="bc983b4d-41d8-5512-9ca8-4ee390bf89c0",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossil.Name",
    display_name="Root Fossil",
    searchable_by=["Root Fossil", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=40,
    passive=ExFossilPassive(),
    abilities=[fossil_discard_ability()],
)
