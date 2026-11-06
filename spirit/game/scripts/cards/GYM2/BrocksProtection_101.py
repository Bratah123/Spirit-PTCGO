from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    brocks_protection, brocks_protection_condition, brocks_protection_passive,
    brocks_protection_targets,
)


card = ItemCardDef(
    guid="9ed498bf-e15e-5592-9623-f8272c4bb34c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksProtection.Name",
    display_name="Brock's Protection",
    searchable_by=["Brock's Protection"],
    subtypes=[],
    collector_number=101,
    set_code="GYM2",
    rarity=Rarities.Rare,
    condition=brocks_protection_condition,
    effect=brocks_protection,
    play_targets=brocks_protection_targets,
    play_target_prompt="Choose a Pokémon with Brock in its name",
)
card.passive = brocks_protection_passive
