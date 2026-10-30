"""STUB: effect not implemented — do not guess mechanics.
Great Ball (DP7 #85): trainer effect stubbed.

Card text:
  - Search your deck for a Basic Pokémon and put it onto your Bench. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7e1b1b8d-6dad-565c-8eb1-5eb1f2c56ecd",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
