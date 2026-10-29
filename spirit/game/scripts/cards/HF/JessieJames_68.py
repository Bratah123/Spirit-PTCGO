from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.hf import jessie_james

card = SupporterCardDef(
    guid="4c177700-8b69-5360-9e46-21af47b77315",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JessieJames.Name",
    display_name="Jessie & James",
    searchable_by=["Jessie & James", "Supporter"],
    subtypes=["Supporter"],
    collector_number=68,
    set_code="HF",
    rarity=Rarities.RareUltra,
    effect=jessie_james,
)
