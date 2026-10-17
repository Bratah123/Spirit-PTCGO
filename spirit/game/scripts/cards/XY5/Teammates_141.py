"""STUB: effect not implemented — do not guess mechanics.
Teammates (XY5 #141): trainer effect stubbed.

Card text:
  - You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn.
  - Search your deck for up to 2 cards and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="846718aa-ccef-5fe9-9a33-647af4f4e0dc",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Teammates.Name",
    display_name="Teammates",
    searchable_by=["Teammates", "Supporter"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
