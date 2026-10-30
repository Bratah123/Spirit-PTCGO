from spirit.game.card_effects.energies import HolonEnergyGLPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2d93658b-72f2-5e3f-9075-40ed10ebf019",
    key="EX15",
    name="Holon Energy GL",
    display_name="Holon Energy GL",
    searchable_by=["Holon Energy GL", "Special"],
    subtypes=["Special"],
    collector_number=85,
    set_code="EX15",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=HolonEnergyGLPassive(),
)
