from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import ClassicDarknessEnergyPassive

card = EnergyCardDef(
    guid="d55b9321-1dca-526d-b19e-a8c990808744",
    key="ECARD2",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=142,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    provides=[[PokemonTypes.DARKNESS]],
    passive=ClassicDarknessEnergyPassive(),
)
