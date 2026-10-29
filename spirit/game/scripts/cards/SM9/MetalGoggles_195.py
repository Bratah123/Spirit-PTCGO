from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    metal_goggles_passive,
)

card = PokemonToolCardDef(
    guid="fbf09001-e3f8-5eda-9b50-3b0f5002656e",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalGoggles.Name",
    display_name="Metal Goggles",
    searchable_by=["Metal Goggles", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=195,
    set_code="SM9",
    rarity=Rarities.RareSecret,
            passive=metal_goggles_passive,
        )
