from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import potion_energy_on_attach

card = EnergyCardDef(
    guid="c8cda228-5eca-5263-b610-d55e26755fdd",
    key="BASE5",
    name="Potion Energy",
    display_name="Potion Energy",
    searchable_by=["Potion Energy", "Special"],
    subtypes=["Special"],
    collector_number=82,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    on_attach=potion_energy_on_attach,
)
