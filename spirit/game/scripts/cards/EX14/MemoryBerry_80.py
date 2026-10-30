from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import memory_berry_granted

card = PokemonToolCardDef(
    guid="bb62c9e2-7d57-58e3-93b6-de161ebf1d8c",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MemoryBerry.Name",
    display_name="Memory Berry",
    searchable_by=["Memory Berry", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=80,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=memory_berry_granted(),
)
