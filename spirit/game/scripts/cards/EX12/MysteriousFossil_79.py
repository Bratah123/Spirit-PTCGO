"""EX12 Legend Maker — Mysterious Fossil fossil trainer.
"""
from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import ExFossilPassive
from spirit.game.card_effects.trainers import fossil_discard_ability


card = FossilItemCardDef(
    guid="2af02f87-56c8-53fe-9489-e2f7aee433cf",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=40,
    passive=ExFossilPassive(),
    abilities=[fossil_discard_ability()],
)
