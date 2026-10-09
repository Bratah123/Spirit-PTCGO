from spirit.game.card_effects.energies import SINGLE_STRIKE_ENERGY
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="a3759d28-263b-58da-96a8-1a4818d21e03",
    key="SWSH5",
    name="Single Strike Energy",
    display_name="Single Strike Energy",
    searchable_by=["Single Strike Energy", "Special", "Single Strike"],
    subtypes=["Special", "Single Strike"],
    collector_number=183,
    set_code="SWSH5",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.FIGHTING,
    is_special=True,
    provides=SINGLE_STRIKE_ENERGY
)
