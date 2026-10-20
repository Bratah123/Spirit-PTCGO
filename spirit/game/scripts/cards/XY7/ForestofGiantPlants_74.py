"""STUB: effect not implemented — do not guess mechanics.
Forest of Giant Plants (XY7 #74): trainer effect stubbed.

Card text:
  - Each player's Grass Pokémon can evolve during his or her first turn or the turn he or she plays those Pokémon.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="aedb9e18-b3de-5561-a0ba-57491ab1a270",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ForestofGiantPlants.Name",
    display_name="Forest of Giant Plants",
    searchable_by=["Forest of Giant Plants", "Stadium"],
    subtypes=["Stadium"],
    collector_number=74,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
