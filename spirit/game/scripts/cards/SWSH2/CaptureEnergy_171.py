from spirit.game.card_effects.energies import capture_on_attach
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7622bd93-cd34-54c4-8104-a93f372d145e",
    key="SWSH2",
    name="Capture Energy",
    display_name="Capture Energy",
    searchable_by=["Capture Energy", "Special"],
    subtypes=["Special"],
    collector_number=171,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=capture_on_attach
)
