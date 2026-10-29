from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm5 import UNIT_ENERGY_GRW

card = EnergyCardDef(
    guid="78ef6670-b1f2-537d-9da9-f631e193cb2f",
    key="SM5",
    name="Unit Energy {G}{R}{W}",
    display_name="Unit Energy {G}{R}{W}",
    searchable_by=["Unit Energy {G}{R}{W}", "Special"],
    subtypes=["Special"],
    collector_number=137,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=UNIT_ENERGY_GRW,
)
