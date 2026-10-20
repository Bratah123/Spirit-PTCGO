"""STUB: effect not implemented — do not guess mechanics.
Energy Reset (XY10 #98): trainer effect stubbed.

Card text:
  - Put as many Energy attached to your Pokémon as you like into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5519f2fa-f23f-5eb2-93b0-9d5d836802de",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyReset.Name",
    display_name="Energy Reset",
    searchable_by=["Energy Reset", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
