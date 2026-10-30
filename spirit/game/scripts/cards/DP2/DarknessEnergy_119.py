"""Darkness Energy (DP2 #119) — Special."""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import SpecialDarknessEnergyPassive

card = EnergyCardDef(
    guid="ba1a27cf-2115-59e6-999f-2226e1823875",
    key="DP2",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=119,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    passive=SpecialDarknessEnergyPassive(),
)
