"""Flash Energy (XY7 #83): scripted (spirit.game.card_effects.xy_energies).

Card text:
  - This card can only be attached to Lightning Pokémon. This card provides Lightning Energy only while this card is attached to a Lightning Pokémon.
  - The Lightning Pokémon this card is attached to has no Weakness.
  - (If this card is attached to anything other than a Lightning Pokémon, discard this card.)
"""

from spirit.game.card_effects.xy_energies import only_type, FlashEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="695127e4-2bf0-5ceb-855f-ed7aea962aa0",
    key="XY7",
    name="Flash Energy",
    display_name="Flash Energy",
    searchable_by=["Flash Energy", "Special"],
    subtypes=["Special"],
    collector_number=83,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=only_type(PokemonTypes.LIGHTNING),
    provides=[[PokemonTypes.LIGHTNING]],
    discard_unless_attach_to=True,
    passive=FlashEnergyPassive(),
)
