from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.trainers import professor_birch_playable


card = SupporterCardDef(
    guid="6dccea49-7207-52db-b670-d04a53c66105",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirch.Name",
    display_name="Professor Birch",
    searchable_by=["Professor Birch", "Supporter"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    condition=professor_birch_playable,
    effect=draw_until_effect(6),
)
