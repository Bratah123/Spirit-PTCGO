from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="cadfe4a4-853d-56c7-904c-2dd342b39545",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CameruptSpiritLink.Name",
    display_name="Camerupt Spirit Link",
    searchable_by=["Camerupt Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=199,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
