"""STUB: effect not implemented — do not guess mechanics.
Team Magma Grunt (TATM #30): trainer effect stubbed.

Card text:
  - Discard a card from your hand. (If you can't discard a card, you can't play this card.) Draw 3 cards. If you discarded a Team Magma Pokémon, draw 1 more card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b70f88dd-ba84-5684-9ca6-03162b5b6181",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaGrunt.Name",
    display_name="Team Magma Grunt",
    searchable_by=["Team Magma Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=30,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
