from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    choice_helmet_passive,
)

card = PokemonToolCardDef(
    guid="44efa97c-7b69-5cd6-b288-8df4b8886d17",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceHelmet.Name",
    display_name="Choice Helmet",
    searchable_by=["Choice Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=229,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    passive=choice_helmet_passive,
)
