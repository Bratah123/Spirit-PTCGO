"""STUB: effect not implemented — do not guess mechanics.
Buddy-Buddy Rescue (XY8 #135): trainer effect stubbed.

Card text:
  - Each player puts a Pokémon from his or her discard pile into his or her hand. (Your opponent chooses first.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="621b05a3-ec94-5aaf-ba07-099dfe7b2b54",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyRescue.Name",
    display_name="Buddy-Buddy Rescue",
    searchable_by=["Buddy-Buddy Rescue", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
