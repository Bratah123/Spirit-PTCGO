from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="151ec0e9-6848-5bce-83a2-9c11147f76fd",
    key="EX13",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
)
