"""STUB: effect not implemented — do not guess mechanics.
Eco Arm (XY7 #71): trainer effect stubbed.

Card text:
  - Shuffle 3 Pokémon Tool cards from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="81b11637-88ca-5d85-8101-26390a2fb766",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EcoArm.Name",
    display_name="Eco Arm",
    searchable_by=["Eco Arm", "Item"],
    subtypes=["Item"],
    collector_number=71,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
