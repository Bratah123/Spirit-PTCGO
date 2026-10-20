from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="1c0005d5-edf2-56fa-a770-e002b2687554",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RayquazaSpiritLink.Name",
    display_name="Rayquaza Spirit Link",
    searchable_by=["Rayquaza Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=87,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
