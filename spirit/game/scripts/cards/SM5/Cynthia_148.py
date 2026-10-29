from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import cynthia

card = SupporterCardDef(
    guid="8ea804bd-9540-5de4-940d-39094d485f4b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=cynthia,
)
