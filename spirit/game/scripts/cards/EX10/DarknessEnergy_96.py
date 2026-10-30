"""EX10 Unseen Forces — Darkness Energy.
"""
from spirit.game.card_effects.energies import DarknessEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="0f7d556d-3f59-5ed8-8029-58a6fadfcbd5",
    key="EX10",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=96,
    set_code="EX10",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    provides=[[PokemonTypes.DARKNESS]],
    passive=DarknessEnergyPassive(),
)
