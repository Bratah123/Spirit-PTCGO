from spirit.game.card_effects.trainers import cyllene, has_discard_card
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9bbc850a-1d68-5b86-946a-1df47fe84512",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cyllene.Name",
    display_name="Cyllene",
    searchable_by=["Cyllene", "Supporter"],
    subtypes=["Supporter"],
    collector_number=201,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    effect=cyllene,
    condition=has_discard_card
)
