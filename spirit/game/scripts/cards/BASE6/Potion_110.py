from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="a8bce0ec-d821-5dea-ae1f-43777c0df211",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion"],
    subtypes=[],
    collector_number=110,
    set_code="BASE6",
    rarity=Rarities.Common,
    condition=requires_damaged_pokemon(),
    effect=heal_item(30)
)
