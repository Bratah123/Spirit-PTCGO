from spirit.game.card_effects.energies import HolonEnergyFFPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="133af4d3-e9df-520d-bc15-3f4f5cd06216",
    key="EX15",
    name="Holon Energy FF",
    display_name="Holon Energy FF",
    searchable_by=["Holon Energy FF", "Special"],
    subtypes=["Special"],
    collector_number=84,
    set_code="EX15",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=HolonEnergyFFPassive(),
)
