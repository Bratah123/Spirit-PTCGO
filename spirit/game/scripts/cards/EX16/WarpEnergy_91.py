from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ex import warp_energy_passive

card = EnergyCardDef(
    guid="689f8aa6-3fe6-5b72-9cfe-d50dafa2025e",
    key="EX16",
    name="Warp Energy",
    display_name="Warp Energy",
    searchable_by=["Warp Energy", "Special"],
    subtypes=["Special"],
    collector_number=91,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=warp_energy_passive(),
)
