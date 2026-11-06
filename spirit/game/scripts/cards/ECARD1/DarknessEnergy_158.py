from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import ClassicDarknessEnergyPassive

card = EnergyCardDef(
    guid="afc3c36b-c875-5e0b-a53a-e0eccf298257",
    key="ECARD1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=158,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    provides=[[PokemonTypes.DARKNESS]],
    passive=ClassicDarknessEnergyPassive(),
)
