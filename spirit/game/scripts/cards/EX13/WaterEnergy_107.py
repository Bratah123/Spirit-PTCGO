from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="49d18d0e-ed74-5cec-a1bb-eca2c0572bc3",
    key="EX13",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.WATER,
    is_special=False,
)
