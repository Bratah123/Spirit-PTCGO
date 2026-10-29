from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import bonnie, bonnie_condition

card = SupporterCardDef(
    guid="6bdc2fce-76e7-5f93-b359-01371a8198be",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bonnie.Name",
    display_name="Bonnie",
    searchable_by=["Bonnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    condition=bonnie_condition,
    effect=bonnie,
)
