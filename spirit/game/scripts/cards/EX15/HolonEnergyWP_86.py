from spirit.game.card_effects.energies import HolonEnergyWPPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c4e565ba-8199-543c-8f27-7d9299b7930d",
    key="EX15",
    name="Holon Energy WP",
    display_name="Holon Energy WP",
    searchable_by=["Holon Energy WP", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="EX15",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=HolonEnergyWPPassive(),
)
