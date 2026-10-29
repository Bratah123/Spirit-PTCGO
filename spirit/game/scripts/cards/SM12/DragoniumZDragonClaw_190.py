from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import DESTRUCTIVE_DRAKE_GX

card = PokemonToolCardDef(
    guid="ea7c61e1-4083-504f-b87a-1f3f72395048",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DragoniumZDragonClaw.Name",
    display_name="Dragonium Z: Dragon Claw",
    searchable_by=["Dragonium Z: Dragon Claw", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=190,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    granted_abilities=[DESTRUCTIVE_DRAKE_GX],
)
