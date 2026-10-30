"""EX13 Holon Phantoms — Dark Metal Energy.
"""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="044d89e6-29a7-5de1-bc55-418027140e2c",
    key="EX13",
    name="Dark Metal Energy",
    display_name="Dark Metal Energy",
    searchable_by=["Dark Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=97,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[
        [PokemonTypes.DARKNESS],
        [PokemonTypes.METAL],
    ],
)
