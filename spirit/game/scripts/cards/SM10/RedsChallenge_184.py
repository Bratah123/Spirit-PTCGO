from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    reds_challenge,
    reds_challenge_condition,
)

card = SupporterCardDef(
    guid="878ce0c1-8979-539b-a8c1-3bbe352c0a68",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedsChallenge.Name",
    display_name="Red's Challenge",
    searchable_by=["Red's Challenge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=184,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    condition=reds_challenge_condition,
    effect=reds_challenge
)
