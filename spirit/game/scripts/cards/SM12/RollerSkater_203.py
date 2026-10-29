from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import roller_skater, roller_skater_condition

card = SupporterCardDef(
    guid="a21675b6-9b09-5d9d-b191-183260ce7063",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkater.Name",
    display_name="Roller Skater",
    searchable_by=["Roller Skater", "Supporter"],
    subtypes=["Supporter"],
    collector_number=203,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=roller_skater, condition=roller_skater_condition,
)
