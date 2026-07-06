from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="93eb2786-94a6-52aa-8faa-49512cc68478",
    key="SWSH6",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=232,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False
)
