from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    fairy_charm_grass_passive,
    is_fairy_pokemon,
)

card = PokemonToolCardDef(
    guid="aea91199-90d4-5f3c-8319-74276b621455",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmGrass.Name",
    display_name="Fairy Charm Grass",
    searchable_by=["Fairy Charm Grass", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=174,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    passive=fairy_charm_grass_passive,
    attach_to=is_fairy_pokemon,
)
