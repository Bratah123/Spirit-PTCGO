from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm4 import MemoryTypePassive

card = PokemonToolCardDef(
    guid="759189e4-6984-573c-89a8-e8c0075647c8",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectricMemory.Name",
    display_name="Electric Memory",
    searchable_by=["Electric Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=121,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    passive=MemoryTypePassive(PokemonTypes.LIGHTNING),
)
