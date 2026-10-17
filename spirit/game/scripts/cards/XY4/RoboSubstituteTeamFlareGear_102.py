"""STUB: effect not implemented — do not guess mechanics.
Robo Substitute Team Flare Gear (XY4 #102): trainer effect stubbed.

Card text:
  - Play this card as if it were a 30 HP Colorless Basic Pokémon. At any time during your turn (before your attack), you may discard this card from play.
  - This card can't retreat. If this card is Knocked Out, your opponent can't take any Prize Cards for it.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8457bcad-af76-541d-a184-e2d862a64b72",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoboSubstituteTeamFlareGear.Name",
    display_name="Robo Substitute Team Flare Gear",
    searchable_by=["Robo Substitute Team Flare Gear", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
