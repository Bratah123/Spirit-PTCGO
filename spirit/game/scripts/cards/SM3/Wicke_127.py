from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import wicke

card = SupporterCardDef(
    guid="e63bb517-bde7-5919-a3b4-d5f6b02fceeb",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wicke.Name",
    display_name="Wicke",
    searchable_by=["Wicke", "Supporter"],
    subtypes=["Supporter"],
    collector_number=127,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=wicke,)
