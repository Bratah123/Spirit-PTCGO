"""Darkness Energy (DP3 #129) — Special."""
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import SpecialDarknessEnergyPassive

card = EnergyCardDef(
    guid="9e97ced3-fd64-57a8-a954-d9fdcaec809c",
    key="DP3",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=129,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    passive=SpecialDarknessEnergyPassive(),
)
