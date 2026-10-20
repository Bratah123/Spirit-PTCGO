"""STUB: effect not implemented — do not guess mechanics.
Parallel City (XY8 #145): trainer effect stubbed.

Card text:
  - Choose which way this card faces before you play it. This ↓ player can't have more than 3 Benched Pokémon. (When this card comes into play, this ↓ player discards Benched Pokémon until he or she has 3 Pokémon on the Bench.)
  - Choose which way this card faces before you play it. Any damage done by attacks from this ↓ player's Grass, Fire, or Water Pokémon is reduced by 20 (before applying Weakness and Resistance).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="77d73cc0-02bd-5f76-af1c-a81dfe223324",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParallelCity.Name",
    display_name="Parallel City",
    searchable_by=["Parallel City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=145,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
