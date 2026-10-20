"""STUB: effect not implemented — do not guess mechanics.
Silent Lab (XY5 #140): trainer effect stubbed.

Card text:
  - Each Basic Pokémon in play, in each player's hand, and in each player's discard pile has no Abilities.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="ff59974c-334d-58fb-bd26-96f35695006e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SilentLab.Name",
    display_name="Silent Lab",
    searchable_by=["Silent Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=140,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
