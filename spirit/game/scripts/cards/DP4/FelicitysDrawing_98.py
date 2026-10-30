"""STUB: effect not implemented — do not guess mechanics.
Felicity's Drawing (DP4 #98): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard up to 2 cards from your hand. If you discard 1 card, draw 3 cards. If you discard 2 cards, draw 4 cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c8485c61-52d1-52ce-b276-6540a31c13a7",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FelicitysDrawing.Name",
    display_name="Felicity's Drawing",
    searchable_by=["Felicity's Drawing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
