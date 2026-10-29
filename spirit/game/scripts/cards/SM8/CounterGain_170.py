from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    counter_gain_passive,
)

card = PokemonToolCardDef(
    guid="4d321b82-ee92-5fa5-93c7-c3a41850d1cc",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterGain.Name",
    display_name="Counter Gain",
    searchable_by=["Counter Gain", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=170,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    passive=counter_gain_passive,
)
