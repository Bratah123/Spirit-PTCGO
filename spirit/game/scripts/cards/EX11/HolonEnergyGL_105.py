from spirit.game.card_effects.energies import HolonEnergyGLPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e2e59f69-c5b7-5b82-a411-a49732188679",
    key="EX11",
    name="Holon Energy GL",
    display_name="Holon Energy GL",
    searchable_by=["Holon Energy GL", "Special"],
    subtypes=["Special"],
    collector_number=105,
    set_code="EX11",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=HolonEnergyGLPassive(),
)
