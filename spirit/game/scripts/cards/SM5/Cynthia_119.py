from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import cynthia

card = SupporterCardDef(
    guid="c996e0ff-54cd-5315-bc79-5af76413ce68",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=cynthia,
)
