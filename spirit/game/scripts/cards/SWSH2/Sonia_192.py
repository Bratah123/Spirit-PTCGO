from spirit.game.card_effects.trainers import sonia
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8cc50741-9eab-5305-b408-c590ce218d0c",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sonia.Name",
    display_name="Sonia",
    searchable_by=["Sonia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=192,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    effect=sonia
)
