from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import bellelba_brycen_man

card = SupporterCardDef(
    guid="138ffcaa-5146-5450-8849-d9e4afb25a84",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BellelbaBrycenMan.Name",
    display_name="Bellelba & Brycen-Man",
    searchable_by=["Bellelba & Brycen-Man", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=186,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=bellelba_brycen_man,
)
