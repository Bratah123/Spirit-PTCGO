from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="961fe2e5-7fe1-5bc4-9079-a98901a6ed54",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GyaradosSpiritLink.Name",
    display_name="Gyarados Spirit Link",
    searchable_by=["Gyarados Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=101,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
