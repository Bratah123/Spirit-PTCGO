"""Wired DP1 trainer."""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import professor_rowan, professor_rowan_condition

card = SupporterCardDef(
    guid="4cf3e77b-6467-5346-9ec7-9ba7aae897be",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorRowan.Name",
    display_name="Professor Rowan",
    searchable_by=["Professor Rowan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    condition=professor_rowan_condition,
    effect=professor_rowan()
)
