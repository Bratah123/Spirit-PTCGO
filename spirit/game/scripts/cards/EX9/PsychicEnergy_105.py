from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ec83f50a-5523-5ceb-8c0e-53405825f03a",
    key="EX9",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
)
