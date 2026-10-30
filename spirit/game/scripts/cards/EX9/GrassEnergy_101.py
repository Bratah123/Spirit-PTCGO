from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4f6d418c-5403-5c48-a6aa-1cbad3b67e21",
    key="EX9",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
)
