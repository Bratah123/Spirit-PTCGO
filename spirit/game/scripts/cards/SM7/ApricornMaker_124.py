from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    apricorn_maker,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="84ac64f4-d478-5575-8ab3-7137074956dc",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornMaker.Name",
    display_name="Apricorn Maker",
    searchable_by=["Apricorn Maker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=apricorn_maker,
    condition=deck_nonempty,
)
