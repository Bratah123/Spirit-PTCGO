from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ec1ef86f-165b-5355-b53f-fdb557866c26",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymTrainer.Name",
    display_name="Gym Trainer",
    searchable_by=["Gym Trainer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="SWSH45",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
