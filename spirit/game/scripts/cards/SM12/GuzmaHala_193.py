from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import guzma_hala

card = SupporterCardDef(
    guid="fdd971e0-c437-596c-a49a-0a92d7b95d86",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GuzmaHala.Name",
    display_name="Guzma & Hala",
    searchable_by=["Guzma & Hala", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=193,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=guzma_hala,
)
