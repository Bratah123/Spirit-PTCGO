"""Pokémon Ranger (XY11 #113).

Card text:
  Remove all effects of attacks on each player and his or her Pokémon.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import pokemon_ranger

card = SupporterCardDef(
    guid="fff76dd0-b469-5592-908d-5dab1cbf9fb5",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonRanger.Name",
    display_name="Pokémon Ranger",
    searchable_by=["Pokémon Ranger", "Supporter"],
    subtypes=["Supporter"],
    collector_number=113,
    set_code="XY11",
    rarity=Rarities.RareUltra,
    effect=pokemon_ranger,
)
