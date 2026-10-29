from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import sophocles, sophocles_condition

card = SupporterCardDef(
    guid="2ffa760e-0269-5e53-bf88-8108384c4f88",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sophocles.Name",
    display_name="Sophocles",
    searchable_by=["Sophocles", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    condition=sophocles_condition,
    effect=sophocles,)
