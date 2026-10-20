from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f14bf81b-b33b-5bbe-a0a6-a04e8032438c",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlalieSpiritLink.Name",
    display_name="Glalie Spirit Link",
    searchable_by=["Glalie Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=139,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
