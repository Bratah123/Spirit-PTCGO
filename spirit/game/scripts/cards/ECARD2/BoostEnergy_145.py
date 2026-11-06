from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import BoostEnergyPassive, is_evolved_pokemon

card = EnergyCardDef(
    guid="de289fd4-2c40-59aa-bb36-35c4e92d2fca",
    key="ECARD2",
    name="Boost Energy",
    display_name="Boost Energy",
    searchable_by=["Boost Energy", "Special"],
    subtypes=["Special"],
    collector_number=145,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
    attach_to=is_evolved_pokemon,
    discard_end_of_attach_turn=True,
    passive=BoostEnergyPassive(),
)
