"""STUB: effect not implemented — do not guess mechanics.
Poké Blower + (DP7 #88): trainer effect stubbed.

Card text:
  - You may play 2 Poké Blower + at the same time. If you play 1 Poké Blower +, flip a coin. If heads, put 1 damage counter on 1 of your opponent's Pokémon. If you play 2 Poké Blower +, choose 1 of your opponent's Benched Pokémon and switch it with 1 of your opponent's Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0c49c6ac-6d99-5347-a613-b05dc7eb95e3",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBlower.Name",
    display_name="Poké Blower +",
    searchable_by=["Pok\u00e9 Blower +", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
