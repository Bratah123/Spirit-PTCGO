from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c8367311-a30c-5f22-903f-c26a7a4e85b7",
    key="BW9",
    name="Plasma Energy",
    display_name="Plasma Energy",
    searchable_by=["Plasma Energy", "Special", "Team Plasma"],
    subtypes=["Special", "Team Plasma"],
    collector_number=106,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
