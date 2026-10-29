from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    hustle_belt_passive,
)

card = PokemonToolCardDef(
    guid="bac1091a-a266-56bc-9231-bd9b8cc614eb",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HustleBelt.Name",
    display_name="Hustle Belt",
    searchable_by=["Hustle Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=179,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    passive=hustle_belt_passive,
)
