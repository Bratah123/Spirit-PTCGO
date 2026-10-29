from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

from spirit.game.card_effects.sm8 import (
    memory_energy_passive,
)

card = EnergyCardDef(
    guid="f72469c6-2c68-59fa-9d02-d4a610e5a512",
    key="SM8",
    name="Memory Energy",
    display_name="Memory Energy",
    searchable_by=["Memory Energy", "Special"],
    subtypes=["Special"],
    collector_number=194,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=memory_energy_passive,
)
