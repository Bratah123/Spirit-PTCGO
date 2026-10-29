from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import lusamine, lusamine_condition

card = SupporterCardDef(
    guid="b4b4351d-1d5f-5d9e-9b70-3cf25f5bfd26",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=153,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=lusamine,
    condition=lusamine_condition,
)
