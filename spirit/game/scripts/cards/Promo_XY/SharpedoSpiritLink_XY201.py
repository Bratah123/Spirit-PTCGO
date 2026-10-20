from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="24a7f124-7f18-5fa3-ae7d-b9066c01728e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SharpedoSpiritLink.Name",
    display_name="Sharpedo Spirit Link",
    searchable_by=["Sharpedo Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=201,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
