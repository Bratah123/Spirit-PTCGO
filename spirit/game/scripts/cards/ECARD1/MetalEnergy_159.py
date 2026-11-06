from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import ClassicMetalEnergyPassive

card = EnergyCardDef(
    guid="eecf2044-33f1-592a-bae9-9ebe70d45c5a",
    key="ECARD1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=159,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    provides=[[PokemonTypes.METAL]],
    passive=ClassicMetalEnergyPassive(),
)
