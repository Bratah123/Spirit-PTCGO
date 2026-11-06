from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_trader, pokemon_trader_condition


card = ItemCardDef(
    guid="6a3860e7-3fd7-5044-8682-f5dd5d92d8c9",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonTrader.Name",
    display_name="Pokémon Trader",
    searchable_by=["Pok\u00e9mon Trader"],
    subtypes=[],
    collector_number=106,
    set_code="BASE4",
    rarity=Rarities.Rare,
    condition=pokemon_trader_condition,
    effect=pokemon_trader,
)
