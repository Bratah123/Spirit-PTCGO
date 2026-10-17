"""STUB: effect not implemented — do not guess mechanics.
Sky Field (XY6 #89): trainer effect stubbed.

Card text:
  - Each player can have 8 Pokémon on his or her Bench.
  - (When this card leaves play, each player discards Benched Pokémon until he or she has 5 Pokémon on the Bench. The owner of this card discards first.)
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="81f06034-e5c6-5c67-b544-9600c2591bfe",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyField.Name",
    display_name="Sky Field",
    searchable_by=["Sky Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
