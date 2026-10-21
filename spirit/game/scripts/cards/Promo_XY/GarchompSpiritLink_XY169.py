from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="965ced53-6273-5689-96a0-b65727349df4",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GarchompSpiritLink.Name",
    display_name="Garchomp Spirit Link",
    searchable_by=["Garchomp Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=169,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
