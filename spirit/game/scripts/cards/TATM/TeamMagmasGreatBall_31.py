"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Great Ball (TATM #31): trainer effect stubbed.

Card text:
  - Search your deck for a Basic Team Magma Pokémon and a basic Fighting Energy card, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="489c8b1b-246c-590e-893e-14738017b7d6",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmasGreatBall.Name",
    display_name="Team Magma's Great Ball",
    searchable_by=["Team Magma's Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=31,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
