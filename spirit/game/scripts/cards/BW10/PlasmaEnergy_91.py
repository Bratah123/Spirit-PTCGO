from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="14e278af-52b9-5f30-b565-86702b59918b",
    key="BW10",
    name="Plasma Energy",
    display_name="Plasma Energy",
    searchable_by=["Plasma Energy", "Special", "Team Plasma"],
    subtypes=["Special", "Team Plasma"],
    collector_number=91,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
