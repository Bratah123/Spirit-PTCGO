"""STUB: effect not implemented — do not guess mechanics.
Audino Spirit Link (XY10 #92): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Audino-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="26df2f58-323a-5027-973f-e8969c4c3fdd",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AudinoSpiritLink.Name",
    display_name="Audino Spirit Link",
    searchable_by=["Audino Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=92,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
