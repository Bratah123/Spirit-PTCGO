from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    fairy_charm_lightning_passive,
)

card = PokemonToolCardDef(
    guid="bf0cb66a-2a98-516e-b038-bd443a6bfa7c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmLightning.Name",
    display_name="Fairy Charm Lightning",
    searchable_by=["Fairy Charm Lightning", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=172,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=fairy_charm_lightning_passive
)
