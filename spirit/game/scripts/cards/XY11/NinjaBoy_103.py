"""STUB: effect not implemented — do not guess mechanics.
Ninja Boy (XY11 #103): trainer effect stubbed.

Card text:
  - Choose 1 of your Basic Pokémon in play. Search your deck for a Basic Pokémon and switch it with that Pokémon. (Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon.) Shuffle the first Pokémon into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c3d648fc-4092-59c9-89a1-ac8b7d792683",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NinjaBoy.Name",
    display_name="Ninja Boy",
    searchable_by=["Ninja Boy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=103,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
