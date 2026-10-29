from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import roller_skater, roller_skater_condition

card = SupporterCardDef(
    guid="c50c4932-c2a5-5d52-be21-8fe62a68b513",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkater.Name",
    display_name="Roller Skater",
    searchable_by=["Roller Skater", "Supporter"],
    subtypes=["Supporter"],
    collector_number=235,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=roller_skater, condition=roller_skater_condition,
)
