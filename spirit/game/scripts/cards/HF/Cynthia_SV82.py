from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import cynthia

card = SupporterCardDef(
    guid="68a06f33-f721-5452-a4c5-0bb6e64f675e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="HF",
    rarity=Rarities.RareUltra,
    effect=cynthia,
)
