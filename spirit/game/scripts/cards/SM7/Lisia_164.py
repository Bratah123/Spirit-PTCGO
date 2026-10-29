from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    lisia,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="505bf65f-28dc-5209-87ed-3c0abc7ebfbf",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lisia.Name",
    display_name="Lisia",
    searchable_by=["Lisia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=164,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=lisia,
    condition=deck_nonempty,
)
