"""Warp Energy (DP7 #95)."""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import warp_energy_on_attach

card = EnergyCardDef(
    guid="5ff65047-c3e8-5678-9a70-78f8937aa84d", key="DP7", name="Warp Energy", display_name="Warp Energy",
    searchable_by=["Warp Energy", "Special"], subtypes=["Special"],
    collector_number=95, set_code="DP7", rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS, is_special=True,
    on_attach=warp_energy_on_attach,
)
