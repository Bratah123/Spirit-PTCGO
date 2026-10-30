from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f081eb4a-3edb-5302-b384-8a2e3cc62492",
    key="EX1",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="EX1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
