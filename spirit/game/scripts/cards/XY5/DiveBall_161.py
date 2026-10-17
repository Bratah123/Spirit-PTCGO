"""STUB: effect not implemented — do not guess mechanics.
Dive Ball (XY5 #161): trainer effect stubbed.

Card text:
  - Search your deck for a Water Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6adcfc8e-7875-5de9-b36d-8f7b2ea10fb6",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DiveBall.Name",
    display_name="Dive Ball",
    searchable_by=["Dive Ball", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="XY5",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
