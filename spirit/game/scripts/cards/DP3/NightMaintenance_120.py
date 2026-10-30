"""STUB: effect not implemented — do not guess mechanics.
Night Maintenance (DP3 #120): trainer effect stubbed.

Card text:
  - Search your discard pile for up to 3 in any combination of Pokémon and basic Energy cards. Show them to your opponent and shuffle them into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="165c29f7-1263-5c87-a6d0-d3e2f40da45d",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightMaintenance.Name",
    display_name="Night Maintenance",
    searchable_by=["Night Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
