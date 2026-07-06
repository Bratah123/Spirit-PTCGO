from spirit.game.card_effects.trainers import hop
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0827d4c2-6ece-5ff0-bb75-55a8a7c15c25",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hop.Name",
    display_name="Hop",
    searchable_by=["Hop", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="SWSH35",
    rarity=Rarities.RareUltra,
    effect=hop
)
