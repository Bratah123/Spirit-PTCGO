from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm12 import draw_energy_on_attach

card = EnergyCardDef(
    guid="9a07c4c8-5d74-5519-8f0c-8fb90a5c3c11",
    key="SM12",
    name="Draw Energy",
    display_name="Draw Energy",
    searchable_by=["Draw Energy", "Special"],
    subtypes=["Special"],
    collector_number=271,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=draw_energy_on_attach,
)
