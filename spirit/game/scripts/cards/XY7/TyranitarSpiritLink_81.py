from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="ce1df9ad-1903-533a-b49d-895a74318263",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TyranitarSpiritLink.Name",
    display_name="Tyranitar Spirit Link",
    searchable_by=["Tyranitar Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=81,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
