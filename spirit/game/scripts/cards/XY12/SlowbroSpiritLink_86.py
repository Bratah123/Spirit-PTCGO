from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="13c4fa65-fa0a-5248-b9f3-1ed5851b8e63",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SlowbroSpiritLink.Name",
    display_name="Slowbro Spirit Link",
    searchable_by=["Slowbro Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=86,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
