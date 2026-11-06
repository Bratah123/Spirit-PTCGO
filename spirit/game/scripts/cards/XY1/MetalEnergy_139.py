from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7ed76d24-456e-5cf8-94bf-5d623256fbfe",
    key="XY1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=139,
    set_code="XY1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False,
)
