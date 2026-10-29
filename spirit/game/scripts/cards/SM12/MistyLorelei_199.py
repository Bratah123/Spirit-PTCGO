from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import misty_lorelei

card = SupporterCardDef(
    guid="b1b4db87-cec7-5c55-84e9-dc8425cca5ee",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistyLorelei.Name",
    display_name="Misty & Lorelei",
    searchable_by=["Misty & Lorelei", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=199,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=misty_lorelei,
)
