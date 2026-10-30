from spirit.game.card_effects.energies import HolonEnergyFFPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="0f2eb03f-7fb1-5ac2-be23-cfd5facb9a59",
    key="EX11",
    name="Holon Energy FF",
    display_name="Holon Energy FF",
    searchable_by=["Holon Energy FF", "Special"],
    subtypes=["Special"],
    collector_number=104,
    set_code="EX11",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=HolonEnergyFFPassive(),
)
