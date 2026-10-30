"""STUB: effect not implemented — do not guess mechanics.
Fossil Excavator (DP5 #82): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck or discard pile for a Trainer card that has Fossil in its name or a Stage 1 or Stage 2 Evolution card that evolves from a Fossil. Show it to your opponent and put it into your hand. If you searched your deck, shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a19dcdd8-24df-5c3f-81dd-dbf181ec5c37",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavator.Name",
    display_name="Fossil Excavator",
    searchable_by=["Fossil Excavator", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
