from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="cd03e426-a73c-507a-a074-20fd9cc0d09f",
    key="EX13",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
)
