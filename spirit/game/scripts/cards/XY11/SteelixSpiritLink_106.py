from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="41d2f013-7517-5d9d-919f-60b12a9c1f7b",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SteelixSpiritLink.Name",
    display_name="Steelix Spirit Link",
    searchable_by=["Steelix Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=106,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
