from spirit.game.card_effects.trainers import rose, has_vmax_in_play
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b5ea3fef-3024-5756-81b2-b4bf302fcae1",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rose.Name",
    display_name="Rose",
    searchable_by=["Rose", "Supporter"],
    subtypes=["Supporter"],
    collector_number=71,
    set_code="SWSH45",
    rarity=Rarities.RareUltra,
    effect=rose,
    condition=has_vmax_in_play
)
