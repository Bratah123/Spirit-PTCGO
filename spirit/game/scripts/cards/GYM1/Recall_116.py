from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import recall


card = ItemCardDef(
    guid="21b819d6-ad55-5873-a6e9-e9ffcc3a01b0",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recall.Name",
    display_name="Recall",
    searchable_by=["Recall"],
    subtypes=[],
    collector_number=116,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=recall,
)
