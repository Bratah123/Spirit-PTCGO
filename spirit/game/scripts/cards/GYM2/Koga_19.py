from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import koga


card = ItemCardDef(
    guid="57d8742f-c836-583f-8d37-3fea4e074b1b",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Koga.Name",
    display_name="Koga",
    searchable_by=["Koga"],
    subtypes=[],
    collector_number=19,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    effect=koga,
)
