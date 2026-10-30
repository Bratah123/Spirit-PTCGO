from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="29aef8ad-a2bf-5eba-b535-8a2f894769ce",
    key="EX13",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
)
