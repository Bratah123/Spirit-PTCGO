from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import meteor_falls_passive

card = StadiumCardDef(
    guid="a9c287b2-8ce4-57df-b1b7-fa7ddfbfe633",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MeteorFalls.Name",
    display_name="Meteor Falls",
    searchable_by=["Meteor Falls", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=meteor_falls_passive(),
)
