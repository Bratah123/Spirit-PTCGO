"""STUB: effect not implemented — do not guess mechanics.
Dawn Stadium (DP5 #79): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Whenever any player attaches an Energy card from his or her hand to Grass Pokémon or Water Pokémon, remove 1 damage counter and all Special Conditions from that Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="5afc6588-d84c-5368-9768-e2deea51b10d",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DawnStadium.Name",
    display_name="Dawn Stadium",
    searchable_by=["Dawn Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=79,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
