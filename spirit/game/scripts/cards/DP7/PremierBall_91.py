"""STUB: effect not implemented — do not guess mechanics.
Premier Ball (DP7 #91): trainer effect stubbed.

Card text:
  - Search your deck or your discard pile for a Pokémon LV.X, show it to your opponent, and put it into your hand. If you search your deck, shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="949300da-ddee-5966-92e3-cdc060912465",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PremierBall.Name",
    display_name="Premier Ball",
    searchable_by=["Premier Ball", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
