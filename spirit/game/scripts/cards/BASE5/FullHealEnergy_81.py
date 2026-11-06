from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import full_heal_energy_on_attach

card = EnergyCardDef(
    guid="4246b06b-7bbd-512d-9fb6-ced009bcbd4c",
    key="BASE5",
    name="Full Heal Energy",
    display_name="Full Heal Energy",
    searchable_by=["Full Heal Energy", "Special"],
    subtypes=["Special"],
    collector_number=81,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    on_attach=full_heal_energy_on_attach,
)
