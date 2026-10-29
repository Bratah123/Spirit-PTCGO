from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import GIANT_HEARTH_ABILITY

card = StadiumCardDef(
    guid="224166b3-5efc-5add-93c4-e4e4473e6622",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantHearth.Name",
    display_name="Giant Hearth",
    searchable_by=["Giant Hearth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=263,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    ability=GIANT_HEARTH_ABILITY,
)
