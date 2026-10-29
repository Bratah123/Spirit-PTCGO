from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import diantha, diantha_condition

card = SupporterCardDef(
    guid="3cc15279-2c3e-50aa-960c-1fc236e33ca7",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Diantha.Name",
    display_name="Diantha",
    searchable_by=["Diantha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    condition=diantha_condition,
    effect=diantha,
)
