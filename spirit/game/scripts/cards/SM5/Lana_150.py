from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import lana

card = SupporterCardDef(
    guid="26e358be-9513-5754-b607-ed8ce789deaf",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lana.Name",
    display_name="Lana",
    searchable_by=["Lana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=lana,)
