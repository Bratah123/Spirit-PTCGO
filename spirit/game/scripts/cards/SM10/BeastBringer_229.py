from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    beast_bringer_passive,
    is_ultra_beast_pokemon,
)

card = PokemonToolCardDef(
    guid="83d5f1c8-103a-5aad-af36-0fc821c360f5",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastBringer.Name",
    display_name="Beast Bringer",
    searchable_by=["Beast Bringer", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=229,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    passive=beast_bringer_passive,
    attach_to=is_ultra_beast_pokemon
)
