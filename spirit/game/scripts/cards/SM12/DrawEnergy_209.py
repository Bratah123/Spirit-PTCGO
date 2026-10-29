from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm12 import draw_energy_on_attach

card = EnergyCardDef(
    guid="7c7935a3-d73a-522c-bf46-4526b76fc27c",
    key="SM12",
    name="Draw Energy",
    display_name="Draw Energy",
    searchable_by=["Draw Energy", "Special"],
    subtypes=["Special"],
    collector_number=209,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=draw_energy_on_attach,
)
