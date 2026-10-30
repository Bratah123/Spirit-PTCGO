from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import space_center_passive

card = StadiumCardDef(
    guid="f4f6c5fa-54c9-547d-a81e-dad8f2747207",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpaceCenter.Name",
    display_name="Space Center",
    searchable_by=["Space Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=space_center_passive(),
)
