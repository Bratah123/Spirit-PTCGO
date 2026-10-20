"""STUB: effect not implemented — do not guess mechanics.
Captivating Poké Puff (XY11 #99): trainer effect stubbed.

Card text:
  - Your opponent reveals his or her hand. Put any number of Basic Pokémon you find there onto your opponent's Bench.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7ca0fb60-d5de-56ff-81e8-3553f6412d94",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CaptivatingPokePuff.Name",
    display_name="Captivating Pok\u00e9 Puff",
    searchable_by=["Captivating Poké Puff", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
