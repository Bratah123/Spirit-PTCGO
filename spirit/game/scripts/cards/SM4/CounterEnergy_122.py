from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm4 import CounterEnergyPassive

card = EnergyCardDef(
    guid="78aeabfd-1bd4-575a-960d-031180c8cd49",
    key="SM4",
    name="Counter Energy",
    display_name="Counter Energy",
    searchable_by=["Counter Energy", "Special"],
    subtypes=["Special"],
    collector_number=122,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=CounterEnergyPassive(),
)
