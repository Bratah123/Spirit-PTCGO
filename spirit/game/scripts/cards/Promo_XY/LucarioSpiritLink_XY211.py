from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f898599a-60e0-536e-a55b-cd59b31e283f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LucarioSpiritLink.Name",
    display_name="Lucario Spirit Link",
    searchable_by=["Lucario Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=211,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
