from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="26df2f58-323a-5027-973f-e8969c4c3fdd",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AudinoSpiritLink.Name",
    display_name="Audino Spirit Link",
    searchable_by=["Audino Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=92,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
