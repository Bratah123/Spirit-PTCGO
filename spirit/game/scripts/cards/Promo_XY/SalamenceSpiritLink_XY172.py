from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="94f2b74f-7dce-5534-b421-e611aa693cfb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SalamenceSpiritLink.Name",
    display_name="Salamence Spirit Link",
    searchable_by=["Salamence Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=172,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
