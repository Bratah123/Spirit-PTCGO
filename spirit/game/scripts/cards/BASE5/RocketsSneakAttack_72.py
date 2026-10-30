from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    rockets_sneak_attack,
    rockets_sneak_attack_condition,
)


card = ItemCardDef(
    guid="ae3caa63-1d33-5ddd-b7df-0a59799625dd",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsSneakAttack.Name",
    display_name="Rocket's Sneak Attack",
    searchable_by=["Rocket's Sneak Attack"],
    subtypes=[],
    collector_number=72,
    set_code="BASE5",
    rarity=Rarities.Rare,
    condition=rockets_sneak_attack_condition,
    effect=rockets_sneak_attack,
)
