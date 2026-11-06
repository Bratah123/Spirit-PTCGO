from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_breeder, pokemon_breeder_condition


card = ItemCardDef(
    guid="16a36a55-836c-5f77-86ae-db29a5e8637c",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder"],
    subtypes=[],
    collector_number=105,
    set_code="BASE4",
    rarity=Rarities.Rare,
    condition=pokemon_breeder_condition,
    effect=pokemon_breeder,
)
