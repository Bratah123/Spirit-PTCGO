from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import fluffy_berry_passive

card = PokemonToolCardDef(
    guid="a3bb14d9-db24-5766-88e3-222cd39b1fb6",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FluffyBerry.Name",
    display_name="Fluffy Berry",
    searchable_by=["Fluffy Berry", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=85,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    passive=fluffy_berry_passive(),
)
