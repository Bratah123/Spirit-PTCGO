from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5a38c6c2-8b4a-5eb3-98ce-096898fc5b87",
    key="EX1",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="EX1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False,
)
