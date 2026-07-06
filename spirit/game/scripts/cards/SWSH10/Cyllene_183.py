from spirit.game.card_effects.trainers import cyllene, has_discard_card
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0430a361-71fc-5cbc-ac62-f324e5b32c40",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cyllene.Name",
    display_name="Cyllene",
    searchable_by=["Cyllene", "Supporter"],
    subtypes=["Supporter"],
    collector_number=183,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    effect=cyllene,
    condition=has_discard_card
)
