from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import blaines_quiz_3, blaines_quiz_3_condition


card = ItemCardDef(
    guid="d3fd7ce7-6607-59d5-bc72-de33ee0ef2e4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuiz3.Name",
    display_name="Blaine's Quiz #3",
    searchable_by=["Blaine's Quiz #3"],
    subtypes=[],
    collector_number=112,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    condition=blaines_quiz_3_condition,
    effect=blaines_quiz_3,
)
