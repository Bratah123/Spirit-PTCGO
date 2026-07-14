from spirit.game.card_effects.trainers import hop
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c2f4517a-c98f-54a2-8c21-14e4362eca87",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hop.Name",
    display_name="Hop",
    searchable_by=["Hop", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    effect=hop
)
