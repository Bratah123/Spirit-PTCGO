from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import will

card = SupporterCardDef(
    guid="768308fd-7a9c-54c9-b11f-6dc17f892fda",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Will.Name",
    display_name="Will",
    searchable_by=["Will", "Supporter"],
    subtypes=["Supporter"],
    collector_number=208,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=will,
)
