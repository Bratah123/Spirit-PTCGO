"""STUB: effect not implemented — do not guess mechanics.
Hand Scope (XY4 #96): trainer effect stubbed.

Card text:
  - Your opponent reveals his or her hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="90f305ed-6ccb-5e8a-9a38-23aa6cc73527",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HandScope.Name",
    display_name="Hand Scope",
    searchable_by=["Hand Scope", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
