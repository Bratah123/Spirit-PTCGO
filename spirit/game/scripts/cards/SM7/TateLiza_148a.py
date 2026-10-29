from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    tate_liza,
    tate_liza_condition,
)

card = SupporterCardDef(
    guid="efd86a39-acdd-5424-b099-5221856a75c3",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TateLiza.Name",
    display_name="Tate & Liza",
    searchable_by=["Tate & Liza", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=tate_liza,
    condition=tate_liza_condition,
)
