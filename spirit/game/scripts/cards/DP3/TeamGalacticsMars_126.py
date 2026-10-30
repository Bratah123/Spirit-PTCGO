"""STUB: effect not implemented — do not guess mechanics.
Team Galactic's Mars (DP3 #126): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw 2 cards. Then, choose a card from your opponent's hand without looking and put it on the bottom of his or her deck.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="3ebd3900-f6d2-51bb-a8ce-032dbdf3ffdb",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamGalacticsMars.Name",
    display_name="Team Galactic's Mars",
    searchable_by=["Team Galactic's Mars", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
