from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f2ed3342-ea03-5e98-954b-538ad8f79f09",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlastoiseSpiritLink.Name",
    display_name="Blastoise Spirit Link",
    searchable_by=["Blastoise Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=73,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
