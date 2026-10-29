from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    fairy_charm_psychic_passive,
    is_fairy_pokemon,
)

card = PokemonToolCardDef(
    guid="25618b26-4e48-57ab-b132-9df0db13e5a7",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmPsychic.Name",
    display_name="Fairy Charm Psychic",
    searchable_by=["Fairy Charm Psychic", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=175,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    passive=fairy_charm_psychic_passive,
    attach_to=is_fairy_pokemon,
)
