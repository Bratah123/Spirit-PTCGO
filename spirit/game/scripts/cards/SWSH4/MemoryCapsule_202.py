from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import MemoryCapsulePassive

card = PokemonToolCardDef(
    guid="1174ee9f-e037-5cbe-9c50-91e08a863f91",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MemoryCapsule.Name",
    display_name="Memory Capsule",
    searchable_by=["Memory Capsule", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=202,
    set_code="SWSH4",
    rarity=Rarities.RareSecret,
    passive=MemoryCapsulePassive(),
)
