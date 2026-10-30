"""Pokémon Ranger (XY11 #104).

Card text:
  Remove all effects of attacks on each player and his or her Pokémon.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import pokemon_ranger

card = SupporterCardDef(
    guid="9f6fdde7-2978-541e-aa87-e53eb07019ce",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonRanger.Name",
    display_name="Pokémon Ranger",
    searchable_by=["Pokémon Ranger", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    effect=pokemon_ranger,
)
