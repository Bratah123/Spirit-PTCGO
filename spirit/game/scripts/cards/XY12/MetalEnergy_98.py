from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5d1a7502-d873-5b28-8bb5-742733a5e29a",
    key="XY12",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="XY12",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False,
)
