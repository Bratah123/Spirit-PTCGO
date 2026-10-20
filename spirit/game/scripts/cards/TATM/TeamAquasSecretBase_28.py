"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Secret Base (TATM #28): trainer effect stubbed.

Card text:
  - The Retreat Cost of each Pokémon in play (except for Team Aqua Pokémon) is Colorless more.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="b153aa0a-2aa0-5609-b220-9f77233a7231",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquasSecretBase.Name",
    display_name="Team Aqua's Secret Base",
    searchable_by=["Team Aqua's Secret Base", "Stadium"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
