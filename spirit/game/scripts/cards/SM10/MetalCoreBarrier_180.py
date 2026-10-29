from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    METAL_CORE_BARRIER_ABILITY,
    is_metal_pokemon,
    metal_core_barrier_passive,
)

card = PokemonToolCardDef(
    guid="358da1fd-9ee6-51b2-b333-c064d5ff1b8d",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalCoreBarrier.Name",
    display_name="Metal Core Barrier",
    searchable_by=["Metal Core Barrier", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=180,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=metal_core_barrier_passive,
    granted_abilities=[METAL_CORE_BARRIER_ABILITY],
    attach_to=is_metal_pokemon
)
