"""STUB: effect not implemented — do not guess mechanics.
Fiery Torch (XY2 #89): trainer effect stubbed.

Card text:
  - Discard a Fire Energy card from your hand. (If you can't discard a Fire Energy card, you can't play this card.) Draw 2 cards.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="681e3241-8931-5029-ad89-4f87f4eac748",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryTorch.Name",
    display_name="Fiery Torch",
    searchable_by=["Fiery Torch", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
