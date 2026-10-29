from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.hf import jessie_james

card = SupporterCardDef(
    guid="1a8dee58-25d1-594a-89ba-717784555890",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JessieJames.Name",
    display_name="Jessie & James",
    searchable_by=["Jessie & James", "Supporter"],
    subtypes=["Supporter"],
    collector_number=58,
    set_code="HF",
    rarity=Rarities.RareHolo,
    effect=jessie_james,
)
