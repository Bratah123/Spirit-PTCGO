"""STUB: effect not implemented — do not guess mechanics.
Chaos Tower (XY10 #94): trainer effect stubbed.

Card text:
  - Choose which way this card faces before you play it. This ↓ player's Pokémon can't be Confused or Poisoned. (If those Pokémon are already Confused or Poisoned, remove those Special Conditions.)
  - Choose which way this card faces before you play it. This ↓ player's Pokémon can't be Asleep or Paralyzed. (If those Pokémon are already Asleep or Paralyzed, remove those Special Conditions.)
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="b261ac6f-3f12-5fb5-ac4d-21f93dfe979d",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaosTower.Name",
    display_name="Chaos Tower",
    searchable_by=["Chaos Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
