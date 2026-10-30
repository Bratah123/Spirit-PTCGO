from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    the_masked_royal,
    the_masked_royal_condition,
)

card = SupporterCardDef(
    guid="82d93bf4-a25f-5210-94ce-bccc27c2168e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheMaskedRoyal.Name",
    display_name="The Masked Royal",
    searchable_by=["The Masked Royal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=139,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=the_masked_royal,
    condition=the_masked_royal_condition,
)
