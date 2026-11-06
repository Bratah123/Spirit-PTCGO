from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_breeder, pokemon_breeder_condition


card = ItemCardDef(
    guid="97b3209d-3558-5ab8-bc27-7be68c60dcd2",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder"],
    subtypes=[],
    collector_number=102,
    set_code="BASE6",
    rarity=Rarities.Rare,
    condition=pokemon_breeder_condition,
    effect=pokemon_breeder,
)
