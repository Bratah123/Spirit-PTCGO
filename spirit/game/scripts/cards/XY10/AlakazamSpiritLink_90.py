from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="681302e4-2283-5bc9-bc88-945720719652",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AlakazamSpiritLink.Name",
    display_name="Alakazam Spirit Link",
    searchable_by=["Alakazam Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=90,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
