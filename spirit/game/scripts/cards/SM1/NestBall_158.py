from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import bench_has_room

card = ItemCardDef(
    guid="65a24798-8212-55c9-81dc-3a6ebdd89e6f",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NestBall.Name",
    display_name="Nest Ball",
    searchable_by=["Nest Ball", "Item"],
    subtypes=["Item"],
    collector_number=158,
    set_code="SM1",
    rarity=Rarities.RareSecret,
    effect=search_to_bench(),
    condition=bench_has_room
)
