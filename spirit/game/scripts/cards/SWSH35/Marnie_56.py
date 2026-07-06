from spirit.game.card_effects.trainers import marnie
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="de552115-b843-501a-a0b7-c53568e61caa",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Marnie.Name",
    display_name="Marnie",
    searchable_by=["Marnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=56,
    set_code="SWSH35",
    rarity=Rarities.RareHolo,
    effect=marnie
)
