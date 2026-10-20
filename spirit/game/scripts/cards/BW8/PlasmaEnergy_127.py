from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="a791728a-217e-5741-817b-6f20d6362269",
    key="BW8",
    name="Plasma Energy",
    display_name="Plasma Energy",
    searchable_by=["Plasma Energy", "Special", "Team Plasma"],
    subtypes=["Special", "Team Plasma"],
    collector_number=127,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
