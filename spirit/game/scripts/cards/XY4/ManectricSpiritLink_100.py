from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="fa812de4-0871-5201-9b8e-53ea9e91f32a",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ManectricSpiritLink.Name",
    display_name="Manectric Spirit Link",
    searchable_by=["Manectric Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=100,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
