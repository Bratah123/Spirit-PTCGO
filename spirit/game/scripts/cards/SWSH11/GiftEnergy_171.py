from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import gift_energy_on_ko

card = EnergyCardDef(
    guid="3dc6246c-26c5-5bef-ac9e-1ad713270e74",
    key="SWSH11",
    name="Gift Energy",
    display_name="Gift Energy",
    searchable_by=["Gift Energy", "Special"],
    subtypes=["Special"],
    collector_number=171,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_carrier_knocked_out=gift_energy_on_ko,
)
