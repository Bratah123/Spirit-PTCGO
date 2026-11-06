from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import cyclone_energy_on_attach

card = EnergyCardDef(
    guid="6298d92c-827a-5b36-92e2-6fd55e82d26f",
    key="ECARD3",
    name="Cyclone Energy",
    display_name="Cyclone Energy",
    searchable_by=["Cyclone Energy", "Special"],
    subtypes=["Special"],
    collector_number=143,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    on_attach=cyclone_energy_on_attach,
)
