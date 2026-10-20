"""STUB: effect not implemented — do not guess mechanics.
Pokémon Ranger (XY11 #104): trainer effect stubbed.

Card text:
  - Remove all effects of attacks on each player and his or her Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9f6fdde7-2978-541e-aa87-e53eb07019ce",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonRanger.Name",
    display_name="Pok\u00e9mon Ranger",
    searchable_by=["Pokémon Ranger", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
