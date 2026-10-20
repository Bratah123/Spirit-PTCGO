from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="2a8eddad-33cc-53b3-adbc-b1517bece3c3",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GalladeSpiritLink.Name",
    display_name="Gallade Spirit Link",
    searchable_by=["Gallade Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=83,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
