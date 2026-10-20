"""STUB: effect not implemented — do not guess mechanics.
Head Ringer Team Flare Hyper Gear (XY4 #97): trainer effect stubbed.

Card text:
  - Attach this Pokemon Tool to 1 of your opponent's Pokemon-EX that doesn't already have a Pokemon Tool attached to it.
  - The attacks of the Pokémon this card is attached to cost Colorless more.
  - When this card is removed from a Pokémon for any reason, put this card in its owner's discard pile.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="dd0394e5-87bb-5405-b88c-f342f6c4b60e",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeadRingerTeamFlareHyperGear.Name",
    display_name="Head Ringer Team Flare Hyper Gear",
    searchable_by=["Head Ringer Team Flare Hyper Gear", "Pokémon Tool F"],
    subtypes=["Pokémon Tool F"],
    collector_number=97,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
