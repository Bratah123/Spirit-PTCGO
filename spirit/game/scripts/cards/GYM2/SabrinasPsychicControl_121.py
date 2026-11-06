from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    sabrinas_psychic_control,
    sabrinas_psychic_control_condition,
)


card = ItemCardDef(
    guid="d334387e-605d-5ab3-8822-41daf02f21b4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasPsychicControl.Name",
    display_name="Sabrina's Psychic Control",
    searchable_by=["Sabrina's Psychic Control"],
    subtypes=[],
    collector_number=121,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    condition=sabrinas_psychic_control_condition,
    effect=sabrinas_psychic_control,
)
