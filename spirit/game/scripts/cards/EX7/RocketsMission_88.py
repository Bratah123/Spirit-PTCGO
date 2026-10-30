from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import rockets_mission

card = SupporterCardDef(
    guid="a8128db5-ddf1-564a-bd3b-a1db9276b1e4",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsMission.Name",
    display_name="Rocket's Mission",
    searchable_by=["Rocket's Mission", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    effect=rockets_mission,
)
