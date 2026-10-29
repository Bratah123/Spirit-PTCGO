from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f4b60a04-7344-54cf-ba98-94f2313cf307",
    key="SM1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=163,
    set_code="SM1",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.METAL,
    is_special=False,
)
