from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="8abac291-21bd-5a5b-b36c-805cb16c68e6",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AerodactylSpiritLink.Name",
    display_name="Aerodactyl Spirit Link",
    searchable_by=["Aerodactyl Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
