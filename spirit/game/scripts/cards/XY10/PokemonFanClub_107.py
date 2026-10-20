"""STUB: effect not implemented — do not guess mechanics.
Pokémon Fan Club (XY10 #107): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 Basic Pokémon, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2cbda0aa-4cf8-523d-80f3-3e5f2417a63c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFanClub.Name",
    display_name="Pok\u00e9mon Fan Club",
    searchable_by=["Pokémon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
