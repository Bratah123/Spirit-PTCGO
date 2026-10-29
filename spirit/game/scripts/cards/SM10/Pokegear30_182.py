from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    pokegear_30,
)

card = ItemCardDef(
    guid="53217e55-56ea-5504-b940-aefcee4d5f36",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokegear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=182,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=pokegear_30
)
