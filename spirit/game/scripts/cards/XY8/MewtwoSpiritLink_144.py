"""STUB: effect not implemented — do not guess mechanics.
Mewtwo Spirit Link (XY8 #144): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Mewtwo-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="42e94428-abd4-539d-ad6b-d0c8f89d9855",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MewtwoSpiritLink.Name",
    display_name="Mewtwo Spirit Link",
    searchable_by=["Mewtwo Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=144,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
