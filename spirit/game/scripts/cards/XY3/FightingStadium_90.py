"""STUB: effect not implemented — do not guess mechanics.
Fighting Stadium (XY3 #90): trainer effect stubbed.

Card text:
  - The attacks of each Fighting Pokémon in play (both yours and your opponent's) do 20 more damage to the Defending Pokémon-EX (before applying Weakness and Resistance).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="d32c8e6b-3a8f-5b02-a431-15c3145fa013",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingStadium.Name",
    display_name="Fighting Stadium",
    searchable_by=["Fighting Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=90,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
