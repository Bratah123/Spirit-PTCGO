from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="96dc96bd-d318-5ed1-b3ea-ebe2482b616a",
    key="SM3",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=167,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
)
