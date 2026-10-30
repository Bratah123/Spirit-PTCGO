"""EX13 Holon Phantoms — Claw Fossil.
"""
from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import ExFossilPassive
from spirit.game.card_effects.trainers import fossil_discard_ability


card = FossilItemCardDef(
    guid="485a4037-00be-58f1-b7c9-8e5915b3ccf4",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClawFossil.Name",
    display_name="Claw Fossil",
    searchable_by=["Claw Fossil", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=40,
    passive=ExFossilPassive(),
    abilities=[fossil_discard_ability()],
)
