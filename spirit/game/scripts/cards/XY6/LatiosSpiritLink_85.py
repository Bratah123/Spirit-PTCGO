from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="75dab4eb-d11f-50a6-b054-0086c77f4437",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LatiosSpiritLink.Name",
    display_name="Latios Spirit Link",
    searchable_by=["Latios Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=85,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
