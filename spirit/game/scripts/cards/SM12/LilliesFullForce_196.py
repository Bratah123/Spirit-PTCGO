from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import lillies_full_force

card = SupporterCardDef(
    guid="c34a3e29-428e-5f49-a6de-279f4999c6e3",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesFullForce.Name",
    display_name="Lillie's Full Force",
    searchable_by=["Lillie's Full Force", "Supporter"],
    subtypes=["Supporter"],
    collector_number=196,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=lillies_full_force,
)
