from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_trader, pokemon_trader_condition


card = ItemCardDef(
    guid="b3553020-045b-563b-b097-f23232244309",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonTrader.Name",
    display_name="Pokémon Trader",
    searchable_by=["Pok\u00e9mon Trader"],
    subtypes=[],
    collector_number=77,
    set_code="BASE1",
    rarity=Rarities.Rare,
    condition=pokemon_trader_condition,
    effect=pokemon_trader,
)
