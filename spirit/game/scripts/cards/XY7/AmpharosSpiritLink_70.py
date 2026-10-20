from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="5d2a67b8-622d-59ef-96e3-98568fd23577",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AmpharosSpiritLink.Name",
    display_name="Ampharos Spirit Link",
    searchable_by=["Ampharos Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=70,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
