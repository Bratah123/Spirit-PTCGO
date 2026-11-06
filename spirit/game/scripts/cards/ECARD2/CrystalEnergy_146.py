from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import CrystalEnergyPassive

card = EnergyCardDef(
    guid="4aa45df5-96c8-5d0d-909a-ccabce153575",
    key="ECARD2",
    name="Crystal Energy",
    display_name="Crystal Energy",
    searchable_by=["Crystal Energy", "Special"],
    subtypes=["Special"],
    collector_number=146,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=CrystalEnergyPassive(),
)
