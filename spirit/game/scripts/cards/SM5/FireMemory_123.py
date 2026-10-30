from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm4 import MemoryTypePassive

card = PokemonToolCardDef(
    guid="8afdad31-00e1-5bda-8783-d78c6d984f70",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireMemory.Name",
    display_name="Fire Memory",
    searchable_by=["Fire Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=123,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    passive=MemoryTypePassive(PokemonTypes.FIRE),
)
