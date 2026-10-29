from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import mars

card = SupporterCardDef(
    guid="995329f5-c227-5f4b-b551-b7e25bef0985",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mars.Name",
    display_name="Mars",
    searchable_by=["Mars", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=mars,
)
