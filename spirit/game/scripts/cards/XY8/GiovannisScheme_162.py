from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.scripts.cards.XY8.GiovannisScheme_138 import giovannis_scheme

card = SupporterCardDef(
    guid="99f6a6a0-4d41-56f2-98ef-0bf1b59ab233",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisScheme.Name",
    display_name="Giovanni's Scheme",
    searchable_by=["Giovanni's Scheme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=162,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    effect=giovannis_scheme
)
