"""STUB: effect not implemented — do not guess mechanics.
Xerosic (XY4 #119): trainer effect stubbed.

Card text:
  - Choose a Pokémon Tool or Special Energy card attached to a Pokémon in play (yours or your opponent's) and discard it.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="d206c0ca-894e-5ece-a6b6-ba5a9761326f",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Xerosic.Name",
    display_name="Xerosic",
    searchable_by=["Xerosic", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
