from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import trash_exchange


card = ItemCardDef(
    guid="6b1ca45d-4d01-5dbe-98b3-f8694877ec7d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrashExchange.Name",
    display_name="Trash Exchange",
    searchable_by=["Trash Exchange"],
    subtypes=[],
    collector_number=126,
    set_code="GYM1",
    rarity=Rarities.Common,
    effect=trash_exchange,
)
