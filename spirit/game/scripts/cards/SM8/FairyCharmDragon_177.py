from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    fairy_charm_dragon_passive,
    is_fairy_pokemon,
)

card = PokemonToolCardDef(
    guid="f0acb0ae-1312-52d1-923d-c1ae1b9ffaf0",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmDragon.Name",
    display_name="Fairy Charm Dragon",
    searchable_by=["Fairy Charm Dragon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=177,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    passive=fairy_charm_dragon_passive,
    attach_to=is_fairy_pokemon,
)
