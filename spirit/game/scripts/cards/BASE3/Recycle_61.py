from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import recycle
from spirit.game.card_effects.trainers import has_discard_card


card = ItemCardDef(
    guid="dc249005-d213-5514-864f-90704c0ca770",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recycle.Name",
    display_name="Recycle",
    searchable_by=["Recycle"],
    subtypes=[],
    collector_number=61,
    set_code="BASE3",
    rarity=Rarities.Common,
    condition=has_discard_card,
    effect=recycle,
)
