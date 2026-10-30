"""Metal Energy (DP5 #95) — Special."""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import SpecialMetalEnergyPassive

card = EnergyCardDef(
    guid="abf26949-3d57-5aba-8faa-0c57be0cdb9f", key="DP5", name="Metal Energy", display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"], subtypes=["Special"],
    collector_number=95, set_code="DP5", rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.METAL, is_special=True,
    passive=SpecialMetalEnergyPassive(),
)
