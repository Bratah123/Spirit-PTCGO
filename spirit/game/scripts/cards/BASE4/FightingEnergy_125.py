from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="47572a91-0cc5-577c-8d95-311631e682fe",
    key="BASE4",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="BASE4",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
