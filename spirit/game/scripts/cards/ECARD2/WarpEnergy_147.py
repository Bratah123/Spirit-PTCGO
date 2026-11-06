from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import warp_energy_on_attach

card = EnergyCardDef(
    guid="e4ba5646-2bd4-5fa3-b05b-d4252c119468",
    key="ECARD2",
    name="Warp Energy",
    display_name="Warp Energy",
    searchable_by=["Warp Energy", "Special"],
    subtypes=["Special"],
    collector_number=147,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    on_attach=warp_energy_on_attach,
)
