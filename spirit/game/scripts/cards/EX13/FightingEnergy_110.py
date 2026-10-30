from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="6d7d742e-5f94-59ac-958e-d26af1386740",
    key="EX13",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
