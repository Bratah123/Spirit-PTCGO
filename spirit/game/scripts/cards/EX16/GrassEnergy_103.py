from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="77e1afdb-3326-50ba-a435-2b01b16111f2",
    key="EX16",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
)
