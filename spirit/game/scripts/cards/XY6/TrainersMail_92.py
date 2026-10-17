"""STUB: effect not implemented — do not guess mechanics.
Trainers' Mail (XY6 #92): trainer effect stubbed.

Card text:
  - Look at the top 4 cards of your deck. You may reveal a Trainer card you find there (except Trainers' Mail) and put it into your hand. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="221140c0-b4a0-53e0-bf40-1ec7ae9aff90",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainersMail.Name",
    display_name="Trainers' Mail",
    searchable_by=["Trainers' Mail", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
