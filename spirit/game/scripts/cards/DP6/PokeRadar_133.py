"""STUB: effect not implemented — do not guess mechanics.
Poké Radar (DP6 #133): trainer effect stubbed.

Card text:
  - Look at the top 5 cards of your deck, choose as many Pokémon as you like, show them to your opponent, and put them into your hand. Put the other cards back on top of your deck. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c8e5bfee-d222-5d51-84c1-ab0b05f1a45a",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeRadar.Name",
    display_name="Poké Radar",
    searchable_by=["Pok\u00e9 Radar", "Item"],
    subtypes=["Item"],
    collector_number=133,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
