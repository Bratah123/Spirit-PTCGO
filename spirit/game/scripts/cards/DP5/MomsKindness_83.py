"""STUB: effect not implemented — do not guess mechanics.
Mom's Kindness (DP5 #83): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw 2 cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b9049447-56cf-5789-a078-177bfe40243d",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MomsKindness.Name",
    display_name="Mom's Kindness",
    searchable_by=["Mom's Kindness", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
