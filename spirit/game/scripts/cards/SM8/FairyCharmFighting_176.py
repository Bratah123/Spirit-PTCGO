from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    fairy_charm_fighting_passive,
    is_fairy_pokemon,
)

card = PokemonToolCardDef(
    guid="d593bdd3-d911-5f18-a563-8b982abb51e9",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmFighting.Name",
    display_name="Fairy Charm Fighting",
    searchable_by=["Fairy Charm Fighting", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=176,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    passive=fairy_charm_fighting_passive,
    attach_to=is_fairy_pokemon,
)
