from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f2560ddc-b6b7-5b0c-8c48-326f739f3942",
    key="CZ",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=155,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False
)
