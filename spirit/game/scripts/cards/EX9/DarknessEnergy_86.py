from spirit.game.card_effects.energies import DarknessEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5ae60ef7-09e1-5e28-add4-8ad286bbdfef",
    key="EX9",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="EX9",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    provides=[[PokemonTypes.DARKNESS]],
    passive=DarknessEnergyPassive(),
)
