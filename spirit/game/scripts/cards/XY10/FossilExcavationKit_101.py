"""STUB: effect not implemented — do not guess mechanics.
Fossil Excavation Kit (XY10 #101): trainer effect stubbed.

Card text:
  - Put 2 in any combination of Helix Fossil Omanyte, Dome Fossil Kabuto, or Old Amber Aerodactyl cards from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0348e1db-4ecb-513f-a4a5-d205e26ab877",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavationKit.Name",
    display_name="Fossil Excavation Kit",
    searchable_by=["Fossil Excavation Kit", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
