from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="85b0afde-b679-5336-a5a3-d02bc4e76729",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GardevoirSpiritLink.Name",
    display_name="Gardevoir Spirit Link",
    searchable_by=["Gardevoir Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=130,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega/Primal Evolution by this name
)
