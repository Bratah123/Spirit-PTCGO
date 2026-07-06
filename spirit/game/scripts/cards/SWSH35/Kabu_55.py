from spirit.game.card_effects.trainers import kabu
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5825a70e-6c3d-5b05-818f-d4d298b8e5f7",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kabu.Name",
    display_name="Kabu",
    searchable_by=["Kabu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=55,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=kabu
)
