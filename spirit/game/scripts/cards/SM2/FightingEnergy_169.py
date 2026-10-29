from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="68536154-a64d-5ffe-b216-b3640a67d647",
    key="SM2",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=169,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
