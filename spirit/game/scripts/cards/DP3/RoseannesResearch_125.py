"""STUB: effect not implemented — do not guess mechanics.
Roseanne's Research (DP3 #125): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 2 in any combination of Basic Pokémon and basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="08e613b5-6a9e-5b82-ab58-d87070f8b593",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoseannesResearch.Name",
    display_name="Roseanne's Research",
    searchable_by=["Roseanne's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=125,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
