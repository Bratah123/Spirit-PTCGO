from spirit.game.card_effects.trainers import sonia
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9ba48959-07bb-569b-aacc-e559e37a4dd1",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sonia.Name",
    display_name="Sonia",
    searchable_by=["Sonia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=203,
    set_code="SWSH2",
    rarity=Rarities.RareRainbow,
    effect=sonia
)
