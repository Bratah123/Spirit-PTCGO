"""STUB: effect not implemented — do not guess mechanics.
Luxury Ball (DP7 #86): trainer effect stubbed.

Card text:
  - Search your deck for a Pokémon (excluding Pokémon LV.X), show it to your opponent, and put it into your hand. Shuffle your deck afterward. If any Luxury Ball is in your discard pile, you can't play this card.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d5c3c385-8cec-58eb-bc2b-aeddcee83f88",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuxuryBall.Name",
    display_name="Luxury Ball",
    searchable_by=["Luxury Ball", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
