from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="dfdaaf6f-f76d-50d3-9cb5-f96775892a35",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AltariaSpiritLink.Name",
    display_name="Altaria Spirit Link",
    searchable_by=["Altaria Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=91,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
