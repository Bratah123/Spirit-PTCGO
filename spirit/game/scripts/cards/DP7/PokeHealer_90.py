"""STUB: effect not implemented — do not guess mechanics.
Poké Healer + (DP7 #90): trainer effect stubbed.

Card text:
  - You may play 2 Poké Healer + at the same time. If you play 1 Poké Healer +, remove 1 damage counter and a Special Condition from 1 of your Active Pokémon. If you play 2 Poké Healer +, remove 8 damage counters and all Special Conditions from 1 of your Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8b781dff-5511-5088-8e93-eee4ccf49dd5",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeHealer.Name",
    display_name="Poké Healer +",
    searchable_by=["Pok\u00e9 Healer +", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
