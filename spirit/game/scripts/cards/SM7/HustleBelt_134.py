from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    hustle_belt_passive,
)

card = PokemonToolCardDef(
    guid="49e3b91b-b484-5d93-947b-c98ce10f2026",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HustleBelt.Name",
    display_name="Hustle Belt",
    searchable_by=["Hustle Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=134,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    passive=hustle_belt_passive,
)
