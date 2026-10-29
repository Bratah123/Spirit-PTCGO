from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import looker, looker_condition

card = SupporterCardDef(
    guid="acf75027-5b78-53db-9607-969dc32f0e29",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Looker.Name",
    display_name="Looker",
    searchable_by=["Looker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=152,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    condition=looker_condition,
    effect=looker,
)
