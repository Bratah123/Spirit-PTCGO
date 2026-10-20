from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="4f4c8a47-ce25-5e47-80b2-a0747557fe79",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MawileSpiritLink.Name",
    display_name="Mawile Spirit Link",
    searchable_by=["Mawile Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=105,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
