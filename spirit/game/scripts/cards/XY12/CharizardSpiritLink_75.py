from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="6eb65d69-d4c2-542e-9b4f-3dd9aa912271",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CharizardSpiritLink.Name",
    display_name="Charizard Spirit Link",
    searchable_by=["Charizard Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=75,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
