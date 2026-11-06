from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    devolution_spray, devolution_spray_condition, devolution_spray_targets,
)


card = ItemCardDef(
    guid="52c43ad2-d597-56ab-8dfc-b616de0256c9",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSpray.Name",
    display_name="Devolution Spray",
    searchable_by=["Devolution Spray"],
    subtypes=[],
    collector_number=72,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=devolution_spray,
    condition=devolution_spray_condition,
    play_targets=devolution_spray_targets,
    play_target_prompt="Choose a Pokémon to devolve",
)
