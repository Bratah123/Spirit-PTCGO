from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import blaines_quiz_1, blaines_quiz_1_condition


card = ItemCardDef(
    guid="0980387e-b82a-5159-9794-b27a35fb763c",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuiz1.Name",
    display_name="Blaine's Quiz #1",
    searchable_by=["Blaine's Quiz #1"],
    subtypes=[],
    collector_number=97,
    set_code="GYM1",
    rarity=Rarities.Rare,
    condition=blaines_quiz_1_condition,
    effect=blaines_quiz_1,
)
