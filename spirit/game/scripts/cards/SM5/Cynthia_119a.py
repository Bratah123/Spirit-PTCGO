from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import cynthia

card = SupporterCardDef(
    guid="64b75b5f-83c1-573e-865f-8cf13b9f667e",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=cynthia,
)
