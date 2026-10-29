from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm5 import SuperBoostEnergyPassive

card = EnergyCardDef(
    guid="2a37d903-7ba4-5b1b-a10c-41793795b9a4",
    key="SM5",
    name="Super Boost Energy {*}",
    display_name="Super Boost Energy {*}",
    searchable_by=["Super Boost Energy {*}", "Special", "Prism Star"],
    subtypes=["Special", "Prism Star"],
    collector_number=136,
    set_code="SM5",
    rarity=Rarities.Prism,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=SuperBoostEnergyPassive(),
)
