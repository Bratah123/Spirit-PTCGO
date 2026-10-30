from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import rockets_hideout_passive

card = StadiumCardDef(
    guid="7b303c09-977b-5677-b49b-b046831085bf",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsHideout.Name",
    display_name="Rocket's Hideout",
    searchable_by=["Rocket's Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=87,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    passive=rockets_hideout_passive(),
)
