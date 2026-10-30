from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    pokemon_personality_test, pokemon_personality_test_condition,
)


card = ItemCardDef(
    guid="58ef2c6c-602e-55ea-b203-84caaafbe1d8",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonPersonalityTest.Name",
    display_name="Pokémon Personality Test",
    searchable_by=["Pok\u00e9mon Personality Test"],
    subtypes=[],
    collector_number=102,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    condition=pokemon_personality_test_condition,
    effect=pokemon_personality_test,
)
