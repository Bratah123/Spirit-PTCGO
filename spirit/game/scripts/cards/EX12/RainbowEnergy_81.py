"""EX12 Legend Maker — Rainbow Energy.
"""
from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME,
    rainbow_energy_on_attach,
)
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities


card = EnergyCardDef(
    guid="4bcc3422-7cc2-5502-aa2f-2146c0b49ada",
    key="EX12",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=81,
    set_code="EX12",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    on_attach=rainbow_energy_on_attach,
)
