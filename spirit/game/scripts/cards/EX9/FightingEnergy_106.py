from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4483adaa-3769-5f09-a056-ade659f65fa0",
    key="EX9",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
