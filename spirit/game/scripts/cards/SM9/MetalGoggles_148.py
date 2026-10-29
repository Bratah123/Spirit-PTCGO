from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    metal_goggles_passive,
)

card = PokemonToolCardDef(
    guid="57d7e7f5-52e6-5255-af70-62d8d97943eb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalGoggles.Name",
    display_name="Metal Goggles",
    searchable_by=["Metal Goggles", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=148,
    set_code="SM9",
    rarity=Rarities.Uncommon,
            passive=metal_goggles_passive,
        )
