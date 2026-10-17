"""STUB: effect not implemented — do not guess mechanics.
Dive Ball (XY5 #125): trainer effect stubbed.

Card text:
  - Search your deck for a Water Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ff945cff-af8d-5a5a-af6e-ba30662bf1fe",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DiveBall.Name",
    display_name="Dive Ball",
    searchable_by=["Dive Ball", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
