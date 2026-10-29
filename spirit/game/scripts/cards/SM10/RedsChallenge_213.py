from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    reds_challenge,
    reds_challenge_condition,
)

card = SupporterCardDef(
    guid="1c25a0e6-dc5b-5480-98b2-48cb7264aa8e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedsChallenge.Name",
    display_name="Red's Challenge",
    searchable_by=["Red's Challenge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=213,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    condition=reds_challenge_condition,
    effect=reds_challenge
)
