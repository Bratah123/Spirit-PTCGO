from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import bench_has_room

card = ItemCardDef(
    guid="2fb45df5-1462-5682-b672-8d8f943fcaa9",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NestBall.Name",
    display_name="Nest Ball",
    searchable_by=["Nest Ball", "Item"],
    subtypes=["Item"],
    collector_number=123,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(),
    condition=bench_has_room
)
