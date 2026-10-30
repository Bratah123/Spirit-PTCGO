"""Metal Energy (DP3 #130) — Special."""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import SpecialMetalEnergyPassive

card = EnergyCardDef(
    guid="c4017d40-500f-5898-b5ac-31b56fb4167e",
    key="DP3",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=130,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    passive=SpecialMetalEnergyPassive(),
)
