from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    rockets_sneak_attack,
    rockets_sneak_attack_condition,
)


card = ItemCardDef(
    guid="38c2c2ae-749d-5f3f-bb8b-85ab5e30693c",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsSneakAttack.Name",
    display_name="Rocket's Sneak Attack",
    searchable_by=["Rocket's Sneak Attack"],
    subtypes=[],
    collector_number=16,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    condition=rockets_sneak_attack_condition,
    effect=rockets_sneak_attack,
)
