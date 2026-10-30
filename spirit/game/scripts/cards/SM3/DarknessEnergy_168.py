from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="bf71359d-48e3-505b-b380-208071397c3e",
    key="SM3",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=168,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
)
