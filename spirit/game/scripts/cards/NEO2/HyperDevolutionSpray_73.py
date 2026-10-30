from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    devolution_spray_condition,
    devolution_spray_targets,
    hyper_devolution_spray,
)


card = ItemCardDef(
    guid="45a8e691-0dd2-5026-8712-8cea3524b029",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HyperDevolutionSpray.Name",
    display_name="Hyper Devolution Spray",
    searchable_by=["Hyper Devolution Spray"],
    subtypes=[],
    collector_number=73,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    effect=hyper_devolution_spray,
    condition=devolution_spray_condition,
    play_targets=devolution_spray_targets,
    play_target_prompt="Choose an evolved Pokémon",
)
