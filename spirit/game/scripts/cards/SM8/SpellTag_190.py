from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    is_psychic_pokemon,
    spell_tag_ko,
)

card = PokemonToolCardDef(
    guid="defcd8b2-4da8-5767-866c-cee06b007692",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpellTag.Name",
    display_name="Spell Tag",
    searchable_by=["Spell Tag", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=190,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=spell_tag_ko,
    attach_to=is_psychic_pokemon,
)
