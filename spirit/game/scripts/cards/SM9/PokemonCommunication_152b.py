from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    pokemon_communication,
    pokemon_communication_condition,
)

card = ItemCardDef(
    guid="da85a310-dfd3-5723-a250-7c435a143672",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pok\u00e9mon Communication", "Item"],
    subtypes=["Item"],
    collector_number=198,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=pokemon_communication,
            condition=pokemon_communication_condition,
        )
