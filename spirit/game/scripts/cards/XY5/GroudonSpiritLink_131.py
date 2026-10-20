from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="0184f277-0cee-5608-ac16-3e719b735552",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GroudonSpiritLink.Name",
    display_name="Groudon Spirit Link",
    searchable_by=["Groudon Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=131,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega/Primal Evolution by this name
)
