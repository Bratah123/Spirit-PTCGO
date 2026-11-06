from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="18d0ecbd-9773-54b3-a02e-b41d581505ad",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScizorSpiritLink.Name",
    display_name="Scizor Spirit Link",
    searchable_by=["Scizor Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=111,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
