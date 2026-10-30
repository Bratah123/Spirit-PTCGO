"""STUB: effect not implemented — do not guess mechanics.
Marley's Request (DP7 #87): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your discard pile for 2 different Trainer, Supporter, or Stadium cards, show them to your opponent, and your opponent chooses 1 of them. Put that card into your hand, and discard the other card. (If all Trainer, Supporter, and Stadium cards in your discard pile have the same name, choose 1 of them. Show that card to your opponent and put it into your hand.)
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="95179315-1d39-5ea7-a6f3-90fbb0befae9",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MarleysRequest.Name",
    display_name="Marley's Request",
    searchable_by=["Marley's Request", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
