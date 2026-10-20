"""STUB: effect not implemented — do not guess mechanics.
Professor's Letter (XY8 #146): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b4a1df6a-1d88-5214-952e-8860e356517b",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsLetter.Name",
    display_name="Professor's Letter",
    searchable_by=["Professor's Letter", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
