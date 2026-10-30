from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.trainers import professor_birch_playable


card = SupporterCardDef(
    guid="bfd15a05-86eb-5f2c-9c21-71dfad37d917",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirch.Name",
    display_name="Professor Birch",
    searchable_by=["Professor Birch", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    condition=professor_birch_playable,
    effect=draw_until_effect(6),
)
