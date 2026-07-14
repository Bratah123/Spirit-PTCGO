from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import bench_has_room, fossil_search, is_rare_fossil

card = SupporterCardDef(
    guid="1713c760-1937-5afc-88bf-f07996103dd8",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CaraLiss.Name",
    display_name="Cara Liss",
    searchable_by=["Cara Liss", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    effect=fossil_search(is_rare_fossil),
    condition=bench_has_room,
)
