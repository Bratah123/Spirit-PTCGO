from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.trainers import professor_birch_playable


card = SupporterCardDef(
    guid="1748a5b1-9726-5e27-b610-ba6f7761305d",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirch.Name",
    display_name="Professor Birch",
    searchable_by=["Professor Birch", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    condition=professor_birch_playable,
    effect=draw_until_effect(6),
)
