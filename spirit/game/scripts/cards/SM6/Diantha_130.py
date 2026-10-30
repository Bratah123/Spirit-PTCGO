from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import diantha, diantha_condition

card = SupporterCardDef(
    guid="357fcd88-9c1a-55d4-8a62-6c00a8960d33",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Diantha.Name",
    display_name="Diantha",
    searchable_by=["Diantha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    condition=diantha_condition,
    effect=diantha,
)
