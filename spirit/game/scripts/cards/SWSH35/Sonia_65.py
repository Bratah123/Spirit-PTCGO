from spirit.game.card_effects.trainers import sonia
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2bb1755c-bf2d-58af-8c3d-57ec7597a1c7",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sonia.Name",
    display_name="Sonia",
    searchable_by=["Sonia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=65,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=sonia
)
