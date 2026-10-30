from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    lt_surges_secret_plan,
    lt_surges_secret_plan_condition,
    secret_plan_granted_abilities,
    secret_plan_passive,
)


card = ItemCardDef(
    guid="a0e81ae8-ebac-5d1c-a34a-374a0ed710d2",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesSecretPlan.Name",
    display_name="Lt. Surge's Secret Plan",
    searchable_by=["Lt. Surge's Secret Plan"],
    subtypes=[],
    collector_number=107,
    set_code="GYM2",
    rarity=Rarities.Rare,
    condition=lt_surges_secret_plan_condition,
    effect=lt_surges_secret_plan,
)
card.passive = secret_plan_passive
card.granted_abilities = secret_plan_granted_abilities
