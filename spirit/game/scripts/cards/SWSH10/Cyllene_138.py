from spirit.game.card_effects.trainers import cyllene, has_discard_card
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2603d513-9228-501f-b693-731ed3aacf29",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cyllene.Name",
    display_name="Cyllene",
    searchable_by=["Cyllene", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=cyllene,
    condition=has_discard_card
)
