from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import desert_shaman

card = SupporterCardDef(
    guid="56a14c5e-dbbf-5d20-b874-4bba005c042b",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DesertShaman.Name",
    display_name="Desert Shaman",
    searchable_by=["Desert Shaman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=desert_shaman,
)
