from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.scripts.cards.XY9.Delinquent_98 import delinquent, delinquent_condition

card = SupporterCardDef(
    guid="f9cc2c7e-cb58-54fd-a6e3-d925953137fb",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Delinquent.Name",
    display_name="Delinquent",
    searchable_by=["Delinquent", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=delinquent,
    condition=delinquent_condition
)
