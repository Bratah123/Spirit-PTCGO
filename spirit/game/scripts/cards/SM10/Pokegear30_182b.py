from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    pokegear_30,
)

card = ItemCardDef(
    guid="5f70a427-2e0b-5c38-a33f-668a24340ce1",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokegear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=236,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=pokegear_30
)
