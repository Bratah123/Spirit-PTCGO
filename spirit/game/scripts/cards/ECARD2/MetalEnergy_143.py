from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import ClassicMetalEnergyPassive

card = EnergyCardDef(
    guid="59f1f8fc-2a7f-59ed-8b7d-57e4c93eb7c4",
    key="ECARD2",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=143,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    provides=[[PokemonTypes.METAL]],
    passive=ClassicMetalEnergyPassive(),
)
