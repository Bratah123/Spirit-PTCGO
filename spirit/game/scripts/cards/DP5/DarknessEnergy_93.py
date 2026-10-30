"""Darkness Energy (DP5 #93) — Special."""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import SpecialDarknessEnergyPassive

card = EnergyCardDef(
    guid="4abaff40-a2a3-50f0-9bee-3598b8fd14aa", key="DP5", name="Darkness Energy", display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"], subtypes=["Special"],
    collector_number=93, set_code="DP5", rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.DARKNESS, is_special=True,
    passive=SpecialDarknessEnergyPassive(),
)
