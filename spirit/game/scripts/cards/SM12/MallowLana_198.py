from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import mallow_lana

card = SupporterCardDef(
    guid="248946ab-8c44-5aca-8a19-e37a50505a08",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MallowLana.Name",
    display_name="Mallow & Lana",
    searchable_by=["Mallow & Lana", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=198,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=mallow_lana,
)
