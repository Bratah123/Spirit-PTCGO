from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="d58378e9-5177-5aa3-8e33-3e99bb9a29ae",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GengarSpiritLink.Name",
    display_name="Gengar Spirit Link",
    searchable_by=["Gengar Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=95,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
