from spirit.game.card_effects.trainers import judge
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="844bb265-b3fe-51da-a98b-c43786c85389",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    effect=judge
)
