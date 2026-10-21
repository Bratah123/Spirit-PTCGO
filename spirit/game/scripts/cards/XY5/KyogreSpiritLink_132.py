from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="35f2feb9-347d-5271-ae27-8a8b3586c8c5",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KyogreSpiritLink.Name",
    display_name="Kyogre Spirit Link",
    searchable_by=["Kyogre Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=132,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega/Primal Evolution by this name
)
