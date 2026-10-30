"""EX12 Legend Maker — React Energy.
"""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities


card = EnergyCardDef(
    guid="b35e59ac-368f-5390-bc3e-3d20d08c4f29",
    key="EX12",
    name="React Energy",
    display_name="React Energy",
    searchable_by=["React Energy", "Special"],
    subtypes=["Special"],
    collector_number=82,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
)
