from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="7e0a1b1a-42f3-51d5-990b-ca969f82c375",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PidgeotSpiritLink.Name",
    display_name="Pidgeot Spirit Link",
    searchable_by=["Pidgeot Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=81,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
