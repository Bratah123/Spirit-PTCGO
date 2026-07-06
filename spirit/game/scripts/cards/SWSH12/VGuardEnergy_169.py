from spirit.game.card_effects.energies import VGuardPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="77d43395-0432-5739-84d4-4581bd0a5a83",
    key="SWSH12",
    name="V Guard Energy",
    display_name="V Guard Energy",
    searchable_by=["V Guard Energy", "Special"],
    subtypes=["Special"],
    collector_number=169,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=VGuardPassive()
)
