from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    grass_memory_passive,
)

card = PokemonToolCardDef(
    guid="de58d6a0-2a29-5daf-8613-9034f83579e3",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrassMemory.Name",
    display_name="Grass Memory",
    searchable_by=["Grass Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=143,
    set_code="SM9",
    rarity=Rarities.Uncommon,
            passive=grass_memory_passive,
        )
