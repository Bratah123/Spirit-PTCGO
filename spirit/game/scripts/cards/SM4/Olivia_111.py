from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import olivia

card = SupporterCardDef(
    guid="8311aa5c-45d0-58a7-8194-c16ff88f14a6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Olivia.Name",
    display_name="Olivia",
    searchable_by=["Olivia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="SM4",
    rarity=Rarities.RareUltra,
    effect=olivia,)
