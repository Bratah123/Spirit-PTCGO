from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import blaines_quiz_2, blaines_quiz_2_condition


card = ItemCardDef(
    guid="35a87a27-b12a-5237-bcda-db283205e1a5",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuiz2.Name",
    display_name="Blaine's Quiz #2",
    searchable_by=["Blaine's Quiz #2"],
    subtypes=[],
    collector_number=111,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    condition=blaines_quiz_2_condition,
    effect=blaines_quiz_2,
)
