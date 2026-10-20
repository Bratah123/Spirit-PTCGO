from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="2c1ddbf0-e0e9-5a3c-a071-52f5553dea7b",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeedrillSpiritLink.Name",
    display_name="Beedrill Spirit Link",
    searchable_by=["Beedrill Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=159,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
