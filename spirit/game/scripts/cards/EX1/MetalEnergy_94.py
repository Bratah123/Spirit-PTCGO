"""EX1 Ruby & Sapphire — Metal Energy.
"""
from spirit.game.card_effects.energies import MetalEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="fa12931b-5b2b-5a1e-9646-db2d695a4222",
    key="EX1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="EX1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    provides=[[PokemonTypes.METAL]],
    passive=MetalEnergyPassive(),
)
