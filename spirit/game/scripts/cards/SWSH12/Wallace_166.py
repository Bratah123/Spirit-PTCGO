from spirit.game.card_effects.trainers import wallace
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="369195eb-ac17-5089-94a8-a95dea8bc898",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wallace.Name",
    display_name="Wallace",
    searchable_by=["Wallace", "Supporter"],
    subtypes=["Supporter"],
    collector_number=166,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    effect=wallace
)
