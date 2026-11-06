from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import restore_fossil

card = ItemCardDef(
    guid="700344c5-f15f-5ebe-9521-a1589c1d91e0",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldAmberAerodactyl.Name",
    display_name="Old Amber Aerodactyl",
    searchable_by=["Old Amber Aerodactyl", "Item"],
    subtypes=["Item"],
    collector_number=97,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=restore_fossil("Aerodactyl")
)
