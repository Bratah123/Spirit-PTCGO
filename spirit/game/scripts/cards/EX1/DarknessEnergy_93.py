"""EX1 Ruby & Sapphire — Darkness Energy.
"""
from spirit.game.card_effects.energies import DarknessEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="9aa84bd8-c64d-5e0a-9dc4-ff9a09a9f0c1",
    key="EX1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=93,
    set_code="EX1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    provides=[[PokemonTypes.DARKNESS]],
    passive=DarknessEnergyPassive(),
)
