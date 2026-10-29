from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import sophocles, sophocles_condition

card = SupporterCardDef(
    guid="121d7b5b-2df7-54ef-b717-d18bb0806535",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sophocles.Name",
    display_name="Sophocles",
    searchable_by=["Sophocles", "Supporter"],
    subtypes=["Supporter"],
    collector_number=65,
    set_code="SL",
    rarity=Rarities.Uncommon,
    condition=sophocles_condition,
    effect=sophocles,)
