from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    beast_bringer_passive,
    is_ultra_beast_pokemon,
)

card = PokemonToolCardDef(
    guid="46315776-88a1-5d3a-93dc-43ae9ecb11d2",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastBringer.Name",
    display_name="Beast Bringer",
    searchable_by=["Beast Bringer", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=164,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=beast_bringer_passive,
    attach_to=is_ultra_beast_pokemon
)
