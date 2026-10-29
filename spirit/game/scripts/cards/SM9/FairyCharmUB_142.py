from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    fairy_charm_ub_passive,
    is_fairy_pokemon,
)

card = PokemonToolCardDef(
    guid="69cc2e46-9d61-5ccf-8927-f5264056f8c5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmUB.Name",
    display_name="Fairy Charm UB",
    searchable_by=["Fairy Charm UB", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=142,
    set_code="SM9",
    rarity=Rarities.Uncommon,
            passive=fairy_charm_ub_passive,
            attach_to=is_fairy_pokemon,
        )
