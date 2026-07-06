from spirit.game.card_effects.trainers import zisu
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="cc8fe147-eed9-5f7e-ad0c-8e3c7171860c",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zisu.Name",
    display_name="Zisu",
    searchable_by=["Zisu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=159,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=zisu
)
