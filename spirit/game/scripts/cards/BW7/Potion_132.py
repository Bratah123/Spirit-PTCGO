from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="7b1ba5c0-a429-58d1-87d7-b5d09a7548cd",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    collector_number=132,
    set_code="BW7",
    rarity=Rarities.Common,
    condition=requires_damaged_pokemon(),
    effect=heal_item(30)
)
