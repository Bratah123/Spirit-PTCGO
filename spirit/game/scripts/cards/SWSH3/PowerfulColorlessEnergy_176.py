from spirit.game.card_effects.energies import PowerfulColorlessPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f38454bf-14b8-5b80-906d-feb90569337c",
    key="SWSH3",
    name="Powerful Colorless Energy",
    display_name="Powerful Colorless Energy",
    searchable_by=["Powerful Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=176,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=PowerfulColorlessPassive()
)
