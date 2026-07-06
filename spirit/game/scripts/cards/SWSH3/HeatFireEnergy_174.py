from spirit.game.card_effects.energies import HeatFirePassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2d92cb2b-50fc-5129-875d-e9ab2a698d74",
    key="SWSH3",
    name="Heat Fire Energy",
    display_name="Heat Fire Energy",
    searchable_by=["Heat Fire Energy", "Special"],
    subtypes=["Special"],
    collector_number=174,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FIRE,
    is_special=True,
    passive=HeatFirePassive()
)
