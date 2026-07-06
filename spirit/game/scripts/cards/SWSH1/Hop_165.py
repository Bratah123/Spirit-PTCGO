from spirit.game.card_effects.trainers import hop
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="17bd642e-82ae-5e42-8bc9-882955948468",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hop.Name",
    display_name="Hop",
    searchable_by=["Hop", "Supporter"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=hop
)
