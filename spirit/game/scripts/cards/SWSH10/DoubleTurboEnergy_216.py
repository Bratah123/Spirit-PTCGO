from spirit.game.card_effects.energies import DoubleTurboPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2841b910-53da-5908-9801-36606fb166b1",
    key="SWSH10",
    name="Double Turbo Energy",
    display_name="Double Turbo Energy",
    searchable_by=["Double Turbo Energy", "Special"],
    subtypes=["Special"],
    collector_number=216,
    set_code="SWSH10",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
    passive=DoubleTurboPassive()
)
