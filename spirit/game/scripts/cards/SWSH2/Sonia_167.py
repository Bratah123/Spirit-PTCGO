from spirit.game.card_effects.trainers import sonia
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2485e941-7455-597f-a0f3-2543d581741a",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sonia.Name",
    display_name="Sonia",
    searchable_by=["Sonia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    effect=sonia
)
