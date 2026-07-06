from spirit.game.card_effects.trainers import judge
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="88aeea63-4935-539e-b694-f00853b8297d",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=235,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=judge
)
