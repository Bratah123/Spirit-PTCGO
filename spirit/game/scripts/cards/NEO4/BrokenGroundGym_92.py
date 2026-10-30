from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import broken_ground_gym_passive


card = StadiumCardDef(
    guid="f33cb209-4280-5b4f-87e8-5ff656b7feb4",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrokenGroundGym.Name",
    display_name="Broken Ground Gym",
    searchable_by=["Broken Ground Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=92,
    set_code="NEO4",
    rarity=Rarities.Rare,
    passive=broken_ground_gym_passive,
)
