from spirit.game.card_effects.energies import speed_lightning_on_attach
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="9ddcc31e-666e-5832-9071-54d5cb2e6bdf",
    key="SWSH2",
    name="Speed Lightning Energy",
    display_name="Speed Lightning Energy",
    searchable_by=["Speed Lightning Energy", "Special"],
    subtypes=["Special"],
    collector_number=173,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=True,
    on_attach=speed_lightning_on_attach
)
