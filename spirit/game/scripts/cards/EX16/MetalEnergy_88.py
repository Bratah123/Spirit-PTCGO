"""EX13 Holon Phantoms — Metal Energy.
"""
from spirit.game.card_effects.energies import MetalEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="19f73ca0-18d9-543d-b755-009a271484cf",
    key="EX16",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=88,
    set_code="EX16",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    provides=[[PokemonTypes.METAL]],
    passive=MetalEnergyPassive(),
)
