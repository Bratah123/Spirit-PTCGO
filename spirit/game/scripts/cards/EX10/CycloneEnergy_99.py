"""EX10 Unseen Forces — Cyclone Energy.
"""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ex import cyclone_energy_on_attach

card = EnergyCardDef(
    guid="81463c45-1d72-584e-a958-b60c1f09708d",
    key="EX10",
    name="Cyclone Energy",
    display_name="Cyclone Energy",
    searchable_by=["Cyclone Energy", "Special"],
    subtypes=["Special"],
    collector_number=99,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    on_attach=cyclone_energy_on_attach,
)
