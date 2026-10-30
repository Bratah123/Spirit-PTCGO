from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import rockets_hideout_passive


card = StadiumCardDef(
    guid="285d5abd-00ed-50d6-903c-6bd5fd3f1cc1",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsHideout.Name",
    display_name="Rocket's Hideout",
    searchable_by=["Rocket's Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=63,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    passive=rockets_hideout_passive,
)
