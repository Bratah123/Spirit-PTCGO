from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import mallow_lana

card = SupporterCardDef(
    guid="d2ddf8ea-890d-57df-a7b8-075d2d50e9df",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MallowLana.Name",
    display_name="Mallow & Lana",
    searchable_by=["Mallow & Lana", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=231,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=mallow_lana,
)
