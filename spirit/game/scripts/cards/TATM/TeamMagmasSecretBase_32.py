"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Secret Base (TATM #32): trainer effect stubbed.

Card text:
  - Whenever any player puts a Basic Pokémon (except for Team Magma Pokémon) from his or her hand onto his or her Bench, put 2 damage counters on that Pokémon.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="00a64349-e0e4-532e-a4fb-89d300f40dbd",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmasSecretBase.Name",
    display_name="Team Magma's Secret Base",
    searchable_by=["Team Magma's Secret Base", "Stadium"],
    subtypes=["Stadium"],
    collector_number=32,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
