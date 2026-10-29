from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import cynthia_caitlin

card = SupporterCardDef(
    guid="b0972c70-b0bb-5a0f-b202-7c91a8bbdb5e",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiaCaitlin.Name",
    display_name="Cynthia & Caitlin",
    searchable_by=["Cynthia & Caitlin", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=228,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=cynthia_caitlin,
)
