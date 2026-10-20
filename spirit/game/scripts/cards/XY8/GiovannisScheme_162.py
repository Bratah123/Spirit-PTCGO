"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Scheme (XY8 #162): trainer effect stubbed.

Card text:
  - Choose 1:
• Draw cards until you have 5 cards in your hand.
• During this turn, your Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="99f6a6a0-4d41-56f2-98ef-0bf1b59ab233",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisScheme.Name",
    display_name="Giovanni's Scheme",
    searchable_by=["Giovanni's Scheme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=162,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
