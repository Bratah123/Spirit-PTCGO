from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.scripts.cards.XY9.Delinquent_98 import delinquent, delinquent_condition

card = SupporterCardDef(
    guid="5555d1d1-0a03-5414-9173-a4cd85caf68d",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Delinquent.Name",
    display_name="Delinquent",
    searchable_by=["Delinquent", "Supporter"],
    subtypes=["Supporter"],
    collector_number=125,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    effect=delinquent,
    condition=delinquent_condition
)
