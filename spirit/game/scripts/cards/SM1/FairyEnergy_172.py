from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d1010ce9-c724-552b-bb5b-52eb21292e10",
    key="SM1",
    name="Fairy Energy",
    display_name="Fairy Energy",
    searchable_by=["Fairy Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=172,
    set_code="SM1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FAIRY,
    is_special=False,
)
