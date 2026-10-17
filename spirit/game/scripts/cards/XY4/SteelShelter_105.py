"""STUB: effect not implemented — do not guess mechanics.
Steel Shelter (XY4 #105): trainer effect stubbed.

Card text:
  - Each Metal Pokémon (both yours and your opponent's) can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pokémon.)
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="32608b93-6a75-5185-88d7-2e7ab660357d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SteelShelter.Name",
    display_name="Steel Shelter",
    searchable_by=["Steel Shelter", "Stadium"],
    subtypes=["Stadium"],
    collector_number=105,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
