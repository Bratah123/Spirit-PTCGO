from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d8aa295c-de48-583e-9cc3-b67a7f12125d",
    key="SWSH7",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=236,
    set_code="SWSH7",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False
)
