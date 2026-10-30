"""STUB: effect not implemented — do not guess mechanics.
Buck's Training (DP6 #130): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw 2 cards. As long as Buck's Training is next to your Active Pokémon, each of your Active Pokémon's attacks does 10 more damage to the Active Pokémon (before applying Weakness and Resistance).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="fa368c4f-f5f1-568a-abd6-199c9a693d29",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BucksTraining.Name",
    display_name="Buck's Training",
    searchable_by=["Buck's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
