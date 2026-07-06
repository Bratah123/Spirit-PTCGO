from spirit.game.card_effects.trainers import rose, has_vmax_in_play
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="efdced6e-916f-50a8-bc12-cd674930d81f",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rose.Name",
    display_name="Rose",
    searchable_by=["Rose", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    effect=rose,
    condition=has_vmax_in_play
)
