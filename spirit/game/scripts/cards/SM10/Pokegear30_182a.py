from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    pokegear_30,
)

card = ItemCardDef(
    guid="be292e28-ece9-597f-bd4b-3e884acb23a1",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokegear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=235,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=pokegear_30
)
