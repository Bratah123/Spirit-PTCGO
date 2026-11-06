from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="df46868a-bfab-5571-afec-ddea0d59691e",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VenusaurSpiritLink.Name",
    display_name="Venusaur Spirit Link",
    searchable_by=["Venusaur Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=89,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
