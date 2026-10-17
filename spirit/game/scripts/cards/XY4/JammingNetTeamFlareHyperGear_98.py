"""STUB: effect not implemented — do not guess mechanics.
Jamming Net Team Flare Hyper Gear (XY4 #98): trainer effect stubbed.

Card text:
  - Attach this Pokemon Tool to 1 of your opponent's Pokemon-EX that doesn't already have a Pokemon Tool attached to it.
  - The attacks of the Pokémon this card is attached to do 20 less damage to all Defending Pokémon (before applying Weakness and Resistance). (Don't apply Weakness and Resistance for Benched Pokémon.)
  - When this card is removed from a Pokémon for any reason, put this card in its owner's discard pile.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="7aa161b2-aaae-5755-a67a-22aa1a51104b",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JammingNetTeamFlareHyperGear.Name",
    display_name="Jamming Net Team Flare Hyper Gear",
    searchable_by=["Jamming Net Team Flare Hyper Gear", "Pokémon Tool F"],
    subtypes=["Pokémon Tool F"],
    collector_number=98,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
