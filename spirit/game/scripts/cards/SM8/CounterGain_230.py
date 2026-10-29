from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    counter_gain_passive,
)

card = PokemonToolCardDef(
    guid="753f151a-3eb7-50d3-8aa2-98a5d0c9213f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterGain.Name",
    display_name="Counter Gain",
    searchable_by=["Counter Gain", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=230,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    passive=counter_gain_passive,
)
