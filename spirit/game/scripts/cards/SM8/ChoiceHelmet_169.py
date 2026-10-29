from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    choice_helmet_passive,
)

card = PokemonToolCardDef(
    guid="00094e70-0dc4-5916-ac71-230c6bf4b10f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceHelmet.Name",
    display_name="Choice Helmet",
    searchable_by=["Choice Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=169,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    passive=choice_helmet_passive,
)
