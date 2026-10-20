"""STUB: effect not implemented — do not guess mechanics.
Pokémon Fan Club (TwentiethAnn #69): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 Basic Pokémon, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="15785734-44ba-5d54-aeb8-a9cf18304c5a",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFanClub.Name",
    display_name="Pok\u00e9mon Fan Club",
    searchable_by=["Pokémon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
