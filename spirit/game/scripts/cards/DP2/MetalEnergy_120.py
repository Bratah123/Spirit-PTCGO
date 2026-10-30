"""Metal Energy (DP2 #120) — Special."""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import SpecialMetalEnergyPassive

card = EnergyCardDef(
    guid="31217450-77ec-5f70-b830-c3afb136f5cc",
    key="DP2",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=120,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    passive=SpecialMetalEnergyPassive(),
)
