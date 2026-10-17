"""STUB: effect not implemented — do not guess mechanics.
Battle Compressor Team Flare Gear (XY4 #92): trainer effect stubbed.

Card text:
  - Search your deck for up to 3 cards and discard them. Shuffle your deck afterward.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2af80aaa-b14a-5472-8a4f-6906f780a5a7",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleCompressorTeamFlareGear.Name",
    display_name="Battle Compressor Team Flare Gear",
    searchable_by=["Battle Compressor Team Flare Gear", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
