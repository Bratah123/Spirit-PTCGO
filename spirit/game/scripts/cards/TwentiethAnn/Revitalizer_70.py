"""STUB: effect not implemented — do not guess mechanics.
Revitalizer (TwentiethAnn #70): trainer effect stubbed.

Card text:
  - Put 2 Grass Pokémon from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="973254e4-58c2-502b-96d2-2ce49008a4bb",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revitalizer.Name",
    display_name="Revitalizer",
    searchable_by=["Revitalizer", "Item"],
    subtypes=["Item"],
    collector_number=70,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
