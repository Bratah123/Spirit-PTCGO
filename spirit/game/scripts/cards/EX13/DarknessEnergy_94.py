"""EX13 Holon Phantoms — Darkness Energy.
"""
from spirit.game.card_effects.energies import DarknessEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d88abdd5-d15f-59bd-a138-4be1dbd402ef",
    key="EX13",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="EX13",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    provides=[[PokemonTypes.DARKNESS]],
    passive=DarknessEnergyPassive(),
)
