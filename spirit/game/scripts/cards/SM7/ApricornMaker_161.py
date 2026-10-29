from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    apricorn_maker,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="22e510d3-8464-514d-8f9d-626260a00a63",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornMaker.Name",
    display_name="Apricorn Maker",
    searchable_by=["Apricorn Maker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=apricorn_maker,
    condition=deck_nonempty,
)
