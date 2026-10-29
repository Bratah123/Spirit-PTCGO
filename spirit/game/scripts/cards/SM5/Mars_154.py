from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import mars

card = SupporterCardDef(
    guid="2b5f706d-5c17-508e-b7c9-48a40b8f2162",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mars.Name",
    display_name="Mars",
    searchable_by=["Mars", "Supporter"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=mars,
)
