"""STUB: effect not implemented — do not guess mechanics.
Devolution Spray (XY12 #76): trainer effect stubbed.

Card text:
  - Devolve 1 of your evolved Pokémon and put the highest Stage Evolution card on it into your hand. (That Pokémon can't evolve this turn.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fffc7ce3-749f-5fa5-94d5-c39526977302",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSpray.Name",
    display_name="Devolution Spray",
    searchable_by=["Devolution Spray", "Item"],
    subtypes=["Item"],
    collector_number=76,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
