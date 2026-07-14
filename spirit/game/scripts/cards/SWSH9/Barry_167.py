from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hop

card = SupporterCardDef(
    guid="259b4249-f054-565c-a414-e5a75db917fd",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Barry.Name",
    display_name="Barry",
    searchable_by=["Barry", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    effect=hop
)
