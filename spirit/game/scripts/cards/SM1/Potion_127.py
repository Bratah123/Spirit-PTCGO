from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="ff99487f-3d00-512b-84ad-15053c84df91",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    condition=requires_damaged_pokemon(),
    effect=heal_item(30)
)
