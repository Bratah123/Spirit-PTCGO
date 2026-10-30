from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_trader, pokemon_trader_condition


card = ItemCardDef(
    guid="c8cf2fe6-09d9-57f9-a12e-b25754f44869",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonTrader.Name",
    display_name="Pokémon Trader",
    searchable_by=["Pok\u00e9mon Trader"],
    subtypes=[],
    collector_number=103,
    set_code="BASE6",
    rarity=Rarities.Rare,
    condition=pokemon_trader_condition,
    effect=pokemon_trader,
)
