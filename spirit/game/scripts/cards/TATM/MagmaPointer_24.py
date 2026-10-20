"""STUB: effect not implemented — do not guess mechanics.
Magma Pointer (TATM #24): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Team Magma Pokémon this card is attached to can also use the attack on this card. (You still need the necessary Energy to use this attack.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="d4dd6f80-a724-57f5-8d0a-a5a149157363",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MagmaPointer.Name",
    display_name="Magma Pointer",
    searchable_by=["Magma Pointer", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=24,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
