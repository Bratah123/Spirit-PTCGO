from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_march


card = ItemCardDef(
    guid="fa51c915-8eac-504b-86a9-c5f695a61cbe",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonMarch.Name",
    display_name="Pokémon March",
    searchable_by=["Pok\u00e9mon March"],
    subtypes=[],
    collector_number=102,
    set_code="NEO1",
    rarity=Rarities.Common,
    effect=pokemon_march
)
