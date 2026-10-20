"""STUB: effect not implemented — do not guess mechanics.
Professor's Letter (XY8 #146a): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="38c48494-617e-54a5-81b8-b4c0e3cdcf77",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsLetter.Name",
    display_name="Professor's Letter",
    searchable_by=["Professor's Letter", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
