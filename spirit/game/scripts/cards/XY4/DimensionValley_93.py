"""STUB: effect not implemented — do not guess mechanics.
Dimension Valley (XY4 #93): trainer effect stubbed.

Card text:
  - Each Psychic Pokémon's attacks (both yours and your opponent's) cost Colorless less.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="915776f2-92b4-53ab-97ad-bcf2d4ce25a9",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DimensionValley.Name",
    display_name="Dimension Valley",
    searchable_by=["Dimension Valley", "Stadium"],
    subtypes=["Stadium"],
    collector_number=93,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
