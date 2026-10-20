"""STUB: effect not implemented — do not guess mechanics.
Here Comes Team Rocket! (XY12 #113): trainer effect stubbed.

Card text:
  - Each player turns all of his or her Prize cards face up. (Those Prize cards remain face up for the rest of the game.)
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f7f04d60-e7bd-5505-afa0-fa7a659625b4",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!", "Supporter"],
    subtypes=["Supporter"],
    collector_number=113,
    set_code="XY12",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
