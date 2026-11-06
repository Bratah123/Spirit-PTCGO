from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    pokemon_breeder_fields,
    pokemon_breeder_fields_condition,
)


card = ItemCardDef(
    guid="8090d85b-69f9-5447-b33f-50706305fadc",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreederFields.Name",
    display_name="Pokémon Breeder Fields",
    searchable_by=["Pok\u00e9mon Breeder Fields"],
    subtypes=[],
    collector_number=62,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    condition=pokemon_breeder_fields_condition,
    effect=pokemon_breeder_fields,
)
