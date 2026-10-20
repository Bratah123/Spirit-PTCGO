"""STUB: effect not implemented — do not guess mechanics.
Shrine of Memories (XY5 #139): trainer effect stubbed.

Card text:
  - Each player's evolved Pokémon can use any attack from its previous Evolutions. (That player still needs the necessary Energy to use each attack.)
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="23a9102a-c29c-510f-a38e-8d8488f7a361",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofMemories.Name",
    display_name="Shrine of Memories",
    searchable_by=["Shrine of Memories", "Stadium"],
    subtypes=["Stadium"],
    collector_number=139,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
