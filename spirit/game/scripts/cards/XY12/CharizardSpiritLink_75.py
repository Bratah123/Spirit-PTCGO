"""STUB: effect not implemented — do not guess mechanics.
Charizard Spirit Link (XY12 #75): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Charizard-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="6eb65d69-d4c2-542e-9b4f-3dd9aa912271",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CharizardSpiritLink.Name",
    display_name="Charizard Spirit Link",
    searchable_by=["Charizard Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=75,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
