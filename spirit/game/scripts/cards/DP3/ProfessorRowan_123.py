"""Wired DP1 trainer."""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import professor_rowan, professor_rowan_condition

card = SupporterCardDef(
    guid="8f3a7c42-53df-530b-b29f-fd96705a4b07",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorRowan.Name",
    display_name="Professor Rowan",
    searchable_by=["Professor Rowan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    condition=professor_rowan_condition,
    effect=professor_rowan()
)
