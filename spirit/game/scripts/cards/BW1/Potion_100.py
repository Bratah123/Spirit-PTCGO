from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="d73ca4da-dd21-f428-8051-264ab564587c",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    collector_number=100,
    set_code="BW1",
    rarity=Rarities.Common,
    condition=requires_damaged_pokemon(),
    effect=heal_item(30)
)
