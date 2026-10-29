from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    pokegear_30,
)

card = ItemCardDef(
    guid="8f3ad3e8-9bdd-5b40-8edb-aa91e9897856",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokegear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=233,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    effect=pokegear_30
)
