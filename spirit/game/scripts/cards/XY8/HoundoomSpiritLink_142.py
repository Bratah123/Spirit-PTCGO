from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="31791748-c246-5d63-b8a0-595fde2b1f25",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HoundoomSpiritLink.Name",
    display_name="Houndoom Spirit Link",
    searchable_by=["Houndoom Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=142,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=None  # the engine keeps the turn on Mega Evolution by this name
)
