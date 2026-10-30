from spirit.game.card_effects.energies import DarknessEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5b8c4f59-1540-5111-a2a2-7fbc26acfafd",
    key="EX11",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=103,
    set_code="EX11",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    provides=[[PokemonTypes.DARKNESS]],
    passive=DarknessEnergyPassive(),
)
