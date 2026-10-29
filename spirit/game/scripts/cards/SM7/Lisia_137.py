from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    lisia,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="170666de-07f5-5edf-9be1-f084cf6c13d1",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lisia.Name",
    display_name="Lisia",
    searchable_by=["Lisia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=lisia,
    condition=deck_nonempty,
)
