from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ex import heal_energy_on_attach

card = EnergyCardDef(
    guid="8032c1e9-5d8b-5d04-8f48-ddff81cbdc5a",
    key="POP4",
    name="Heal Energy",
    display_name="Heal Energy",
    searchable_by=["Heal Energy", "Special"],
    subtypes=["Special"],
    collector_number=8,
    set_code="POP4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    on_attach=heal_energy_on_attach,
)
