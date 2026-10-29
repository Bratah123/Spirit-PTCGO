from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    stealthy_hood_passive,
)

card = PokemonToolCardDef(
    guid="54bb7825-24ff-5e2d-bc5f-48985460adc4",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StealthyHood.Name",
    display_name="Stealthy Hood",
    searchable_by=["Stealthy Hood", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=186,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=stealthy_hood_passive
)
