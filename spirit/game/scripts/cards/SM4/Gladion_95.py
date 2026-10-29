from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import gladion, has_prizes_remaining

card = SupporterCardDef(
    guid="b43d09c8-ab22-5d3b-af7f-6f3481608951",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gladion.Name",
    display_name="Gladion",
    searchable_by=["Gladion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=gladion,
    condition=has_prizes_remaining,
)
