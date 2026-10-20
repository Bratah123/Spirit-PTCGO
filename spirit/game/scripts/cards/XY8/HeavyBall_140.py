"""STUB: effect not implemented — do not guess mechanics.
Heavy Ball (XY8 #140): trainer effect stubbed.

Card text:
  - Search your deck for a Pokémon with a Retreat Cost of 3 or more, reveal it, and put it into your hand. Shuffle your deck afterward.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ce38bce3-5702-5c19-991b-8dbde226fcea",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBall.Name",
    display_name="Heavy Ball",
    searchable_by=["Heavy Ball", "Item"],
    subtypes=["Item"],
    collector_number=140,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
