"""Multi Energy (DP2 #118)."""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import MULTI_ENERGY_PROVIDES, MultiEnergyPassive

card = EnergyCardDef(
    guid="49783afe-738c-5a8a-b4e6-09563b25fc8a",
    key="DP2",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=118,
    set_code="DP2",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=MULTI_ENERGY_PROVIDES,
    passive=MultiEnergyPassive(),
)
