"""STUB: effect not implemented — do not guess mechanics.
Bebe's Search (DP3 #119): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Choose a card from your hand and put it on top of your deck. Search your deck for a Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward. (If this is the only card in your hand, you can't play this card.)
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8cd29d02-abbe-5656-87d4-2427ea69e190",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BebesSearch.Name",
    display_name="Bebe's Search",
    searchable_by=["Bebe's Search", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
