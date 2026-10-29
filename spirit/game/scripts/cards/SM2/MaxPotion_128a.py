from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_damaged_pokemon
from spirit.game.scripts.cards.SM2.MaxPotion_128 import max_potion

card = ItemCardDef(
    guid="17eebe32-6e11-5f1b-95c3-b6073cd4322b",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=178,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=requires_damaged_pokemon(),
    effect=max_potion,
)
