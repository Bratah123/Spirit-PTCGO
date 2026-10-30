"""EX10 Unseen Forces — Metal Energy.
"""
from spirit.game.card_effects.energies import MetalEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="91e9fad7-e694-5386-9b87-44ffe4e13e6b",
    key="EX10",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=97,
    set_code="EX10",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    provides=[[PokemonTypes.METAL]],
    passive=MetalEnergyPassive(),
)
