from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="130f58ae-d2c2-558e-aab4-871c5b1a2a91",
    key="CZ",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=159,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    energy_type=PokemonTypes.METAL,
    is_special=False
)
