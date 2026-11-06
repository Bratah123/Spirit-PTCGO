from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="10fcc41f-db20-5a45-8a20-c144cb23836a",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SceptileSpiritLink.Name",
    display_name="Sceptile Spirit Link",
    searchable_by=["Sceptile Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=80,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
