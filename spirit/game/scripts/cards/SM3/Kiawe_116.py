from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import kiawe

card = SupporterCardDef(
    guid="be3ca5ba-43d8-5792-9d4c-6d4ea7da4d07",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kiawe.Name",
    display_name="Kiawe",
    searchable_by=["Kiawe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=116,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=kiawe,)
