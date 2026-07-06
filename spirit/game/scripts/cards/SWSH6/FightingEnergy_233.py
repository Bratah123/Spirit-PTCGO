from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="1c0bdf03-d3f9-5160-bcc9-e34d61b582a2",
    key="SWSH6",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=233,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False
)
