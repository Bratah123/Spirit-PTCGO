from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="cde082ce-0988-548a-8c14-55de65d884b6",
    key="EX7",
    name="Dark Metal Energy",
    display_name="Dark Metal Energy",
    searchable_by=["Dark Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[
        [PokemonTypes.DARKNESS],
        [PokemonTypes.METAL],
    ],
)
