from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import MemoryCapsulePassive

card = PokemonToolCardDef(
    guid="b891cd7c-3b67-56ea-a84e-a0065e194be6",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MemoryCapsule.Name",
    display_name="Memory Capsule",
    searchable_by=["Memory Capsule", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=155,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    passive=MemoryCapsulePassive(),
)
