"""EX13 Holon Phantoms — Mysterious Fossil.
"""
from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import ExFossilPassive
from spirit.game.card_effects.trainers import fossil_discard_ability


card = FossilItemCardDef(
    guid="099c29e6-93bb-5b05-b70d-e54ba6f5edfb",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=40,
    passive=ExFossilPassive(),
    abilities=[fossil_discard_ability()],
)
