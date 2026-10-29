from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d071af21-0a19-5440-b5c7-5a9b9bf0d59b",
    key="SM2",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=167,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
)
