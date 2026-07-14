from spirit.game.card_effects.trainers import thorton, thorton_condition
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2df481e2-a527-5e60-8547-e65daca8bfc4",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Thorton.Name",
    display_name="Thorton",
    searchable_by=["Thorton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    condition=thorton_condition,
    effect=thorton,
)
