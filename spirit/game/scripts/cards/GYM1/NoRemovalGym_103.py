from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import no_removal_gym_passive


card = StadiumCardDef(
    guid="e6c8a31a-483c-5f9b-968c-9ee76b7c4710",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NoRemovalGym.Name",
    display_name="No Removal Gym",
    searchable_by=["No Removal Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=103,
    set_code="GYM1",
    rarity=Rarities.Rare,
    passive=no_removal_gym_passive,
)
