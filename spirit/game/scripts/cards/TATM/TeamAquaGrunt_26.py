"""STUB: effect not implemented — do not guess mechanics.
Team Aqua Grunt (TATM #26): trainer effect stubbed.

Card text:
  - Discard a card from your hand. (If you can't discard a card, you can't play this card.) Draw 3 cards. If you discarded a Team Aqua Pokémon, draw 1 more card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8f7dd117-d369-5ae5-8de7-598a8da25c9c",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaGrunt.Name",
    display_name="Team Aqua Grunt",
    searchable_by=["Team Aqua Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=26,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
