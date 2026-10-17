"""STUB: effect not implemented — do not guess mechanics.
Repeat Ball (XY5 #136): trainer effect stubbed.

Card text:
  - Search your deck for a Pokémon with the same name as 1 of your Pokémon in play, reveal it, and put it into your hand. Shuffle your deck afterward.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="599e6d4f-7a60-578c-a17d-20f2d1c1eef0",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RepeatBall.Name",
    display_name="Repeat Ball",
    searchable_by=["Repeat Ball", "Item"],
    subtypes=["Item"],
    collector_number=136,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
