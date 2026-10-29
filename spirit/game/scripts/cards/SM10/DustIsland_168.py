from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    dust_island_passive,
)

card = StadiumCardDef(
    guid="cf6a3667-cbcc-5ead-b1ec-1ad793af782e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DustIsland.Name",
    display_name="Dust Island",
    searchable_by=["Dust Island", "Stadium"],
    subtypes=["Stadium"],
    collector_number=168,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=dust_island_passive
)
