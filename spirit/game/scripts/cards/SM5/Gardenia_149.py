from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import gardenia, gardenia_condition

card = SupporterCardDef(
    guid="d8030c3d-d696-5ca4-ad82-9480ea2213c8",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gardenia.Name",
    display_name="Gardenia",
    searchable_by=["Gardenia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    condition=gardenia_condition,
    effect=gardenia,
)
