from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="42e94428-abd4-539d-ad6b-d0c8f89d9855",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MewtwoSpiritLink.Name",
    display_name="Mewtwo Spirit Link",
    searchable_by=["Mewtwo Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=144,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
