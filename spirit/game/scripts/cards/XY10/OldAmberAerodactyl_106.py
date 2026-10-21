from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import restore_fossil

card = ItemCardDef(
    guid="c6afbafe-eec4-5ff8-a20d-f0e3401dac8b",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldAmberAerodactyl.Name",
    display_name="Old Amber Aerodactyl",
    searchable_by=["Old Amber Aerodactyl", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=restore_fossil("Aerodactyl")
)
