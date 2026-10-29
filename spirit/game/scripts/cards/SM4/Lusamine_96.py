from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import lusamine, lusamine_condition

card = SupporterCardDef(
    guid="818de1d4-6a4e-585f-af57-b03b0b3a7dd9",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=96,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=lusamine,
    condition=lusamine_condition,
)
