from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f77d9ee0-9cce-5327-b761-1daf01b36b05",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AggronSpiritLink.Name",
    display_name="Aggron Spirit Link",
    searchable_by=["Aggron Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=123,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega/Primal Evolution by this name
)
