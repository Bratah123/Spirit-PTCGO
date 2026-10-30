"""STUB: effect not implemented — do not guess mechanics.
Moonlight Stadium (DP4 #100): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - The Retreat Cost for each Psychic and Darkness Pokémon (both yours and your opponent's) is 0.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="d2e3ee59-6e9b-5d3a-9458-91b129af9275",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MoonlightStadium.Name",
    display_name="Moonlight Stadium",
    searchable_by=["Moonlight Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=100,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
