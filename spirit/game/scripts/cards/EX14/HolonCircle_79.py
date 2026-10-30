from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import holon_circle_passive

card = StadiumCardDef(
    guid="d6e83b9b-8fce-5f14-bf59-35ad8e4b809d",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonCircle.Name",
    display_name="Holon Circle",
    searchable_by=["Holon Circle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=79,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=holon_circle_passive(),
)
