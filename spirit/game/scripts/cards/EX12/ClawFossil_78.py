"""EX12 Legend Maker — Claw Fossil fossil trainer.
"""
from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import ExFossilPassive
from spirit.game.card_effects.trainers import fossil_discard_ability


card = FossilItemCardDef(
    guid="aee83d9e-a5bf-5997-afc9-1ce9e915d4f5",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClawFossil.Name",
    display_name="Claw Fossil",
    searchable_by=["Claw Fossil", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=40,
    passive=ExFossilPassive(),
    abilities=[fossil_discard_ability()],
)
