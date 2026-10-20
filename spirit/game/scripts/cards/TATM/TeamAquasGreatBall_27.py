"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Great Ball (TATM #27): trainer effect stubbed.

Card text:
  - Search your deck for a Basic Team Aqua Pokémon and a basic Water Energy card, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="67503eb2-c932-5f2f-8aca-6f0c3aea29b6",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquasGreatBall.Name",
    display_name="Team Aqua's Great Ball",
    searchable_by=["Team Aqua's Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=27,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
