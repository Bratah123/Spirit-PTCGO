from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import someone_has_bench
from spirit.game.card_effects.ecard import double_gust


card = ItemCardDef(
    guid="573a33f6-0b84-52c8-8685-e57e533c76f6",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DoubleGust.Name",
    display_name="Double Gust",
    searchable_by=["Double Gust"],
    subtypes=[],
    collector_number=100,
    set_code="NEO1",
    rarity=Rarities.Common,
    condition=someone_has_bench,
    effect=double_gust,
)
