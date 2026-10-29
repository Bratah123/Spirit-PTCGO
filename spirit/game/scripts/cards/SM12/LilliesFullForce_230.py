from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import lillies_full_force

card = SupporterCardDef(
    guid="ffa2f0e4-f690-5351-884d-4eeab6b5e2e2",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesFullForce.Name",
    display_name="Lillie's Full Force",
    searchable_by=["Lillie's Full Force", "Supporter"],
    subtypes=["Supporter"],
    collector_number=230,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=lillies_full_force,
)
