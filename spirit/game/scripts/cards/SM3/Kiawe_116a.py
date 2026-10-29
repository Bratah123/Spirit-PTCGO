from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import kiawe

card = SupporterCardDef(
    guid="130e957e-5c0a-5723-a7b3-98f01e283537",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kiawe.Name",
    display_name="Kiawe",
    searchable_by=["Kiawe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=kiawe,)
