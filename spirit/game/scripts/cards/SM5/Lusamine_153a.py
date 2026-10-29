from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import lusamine, lusamine_condition

card = SupporterCardDef(
    guid="d8fddfb2-f391-52fa-b8bc-f39586a2e960",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=lusamine,
    condition=lusamine_condition,
)
