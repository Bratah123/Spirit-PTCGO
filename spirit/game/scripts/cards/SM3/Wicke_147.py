from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import wicke

card = SupporterCardDef(
    guid="ce73b5ae-ab8e-5a5e-857e-2e9d2280e2e0",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wicke.Name",
    display_name="Wicke",
    searchable_by=["Wicke", "Supporter"],
    subtypes=["Supporter"],
    collector_number=147,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    effect=wicke,)
