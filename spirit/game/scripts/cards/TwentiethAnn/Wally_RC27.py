"""STUB: effect not implemented — do not guess mechanics.
Wally (TwentiethAnn #RC27): trainer effect stubbed.

Card text:
  - Search your deck for a card that evolves from 1 of your Pokémon (excluding Pokémon-EX) and put it onto that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward. You can use this card during your first turn or on a Pokémon that was put into play this turn.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b5cb4fd0-47bb-5f4a-aa12-ab674497aecd",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wally.Name",
    display_name="Wally",
    searchable_by=["Wally", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
