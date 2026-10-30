"""STUB: effect not implemented — do not guess mechanics.
Cynthia's Feelings (DP6 #131): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Shuffle your hand into your deck. Then, draw 4 cards. If any of your Pokémon were Knocked Out during your opponent's last turn, draw 4 more cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="51f05ec6-3d35-56d4-b3d2-9d30a7677fc3",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasFeelings.Name",
    display_name="Cynthia's Feelings",
    searchable_by=["Cynthia's Feelings", "Supporter"],
    subtypes=["Supporter"],
    collector_number=131,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
