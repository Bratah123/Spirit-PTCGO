"""STUB: effect not implemented — do not guess mechanics.
Target Whistle Team Flare Gear (XY4 #106): trainer effect stubbed.

Card text:
  - Put a Basic Pokémon from your opponent's discard pile onto his or her Bench.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2ba5e8c2-2986-59c8-936b-af875bdf0431",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TargetWhistleTeamFlareGear.Name",
    display_name="Target Whistle Team Flare Gear",
    searchable_by=["Target Whistle Team Flare Gear", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
