from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="be517dec-0fc2-58e3-a1e3-4ead69e2bfd1",
    key="XY12",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="XY12",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
)
