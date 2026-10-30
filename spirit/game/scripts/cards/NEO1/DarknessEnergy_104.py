"""Darkness Energy (NEO1 #104).

Card text:
  If the Pokémon Darkness Energy is attached to damages the Defending Pokémon
  (after applying Weakness and Resistance), the attack does 10 more damage to
  the Defending Pokémon. At the end of every turn, put 1 damage counter on the
  Pokémon Darkness Energy is attached to, unless it's Darkness or has Dark in
  its name.
  Darkness Energy provides Darkness Energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import ClassicDarknessEnergyPassive

card = EnergyCardDef(
    guid="b12d049a-5483-58fb-ab91-baefc225e9b7",
    key="NEO1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=104,
    set_code="NEO1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    passive=ClassicDarknessEnergyPassive(),
)
