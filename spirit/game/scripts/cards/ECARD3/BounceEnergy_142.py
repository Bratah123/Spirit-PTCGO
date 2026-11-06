from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import bounce_energy_attach_to, bounce_energy_on_attach


card = EnergyCardDef(
    guid="211abfd4-15dd-55e5-a362-46f2c7f70ac8",
    key="ECARD3",
    name="Bounce Energy",
    display_name="Bounce Energy",
    searchable_by=["Bounce Energy", "Special"],
    subtypes=["Special"],
    collector_number=142,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
    attach_to=bounce_energy_attach_to,
    on_attach=bounce_energy_on_attach,
)
