from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import guzma_hala

card = SupporterCardDef(
    guid="0cc365dd-1358-59a7-9898-886d34efdcd8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GuzmaHala.Name",
    display_name="Guzma & Hala",
    searchable_by=["Guzma & Hala", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=229,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=guzma_hala,
)
