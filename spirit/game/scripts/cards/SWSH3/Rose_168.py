from spirit.game.card_effects.trainers import rose, has_vmax_in_play
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="514405a2-9860-5560-b2bb-e1538dbaf3c4",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rose.Name",
    display_name="Rose",
    searchable_by=["Rose", "Supporter"],
    subtypes=["Supporter"],
    collector_number=168,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    effect=rose,
    condition=has_vmax_in_play
)
