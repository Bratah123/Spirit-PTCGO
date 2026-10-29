from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    pokemon_communication,
    pokemon_communication_condition,
)

card = ItemCardDef(
    guid="681c1ae2-9c08-5a42-a565-e968bb722190",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pok\u00e9mon Communication", "Item"],
    subtypes=["Item"],
    collector_number=196,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    effect=pokemon_communication,
            condition=pokemon_communication_condition,
        )
