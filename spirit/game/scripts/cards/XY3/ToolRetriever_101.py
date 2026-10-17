"""STUB: effect not implemented — do not guess mechanics.
Tool Retriever (XY3 #101): trainer effect stubbed.

Card text:
  - Choose up to 2 Pokémon Tool cards attached to your Pokémon and put them into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b7c58442-1e30-51b9-b283-f08a6b335f2e",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolRetriever.Name",
    display_name="Tool Retriever",
    searchable_by=["Tool Retriever", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
