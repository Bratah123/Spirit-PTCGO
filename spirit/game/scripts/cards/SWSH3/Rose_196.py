from spirit.game.card_effects.trainers import rose, has_vmax_in_play
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="809cb0a5-120c-5778-af02-e8d4daad452b",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rose.Name",
    display_name="Rose",
    searchable_by=["Rose", "Supporter"],
    subtypes=["Supporter"],
    collector_number=196,
    set_code="SWSH3",
    rarity=Rarities.RareRainbow,
    effect=rose,
    condition=has_vmax_in_play
)
