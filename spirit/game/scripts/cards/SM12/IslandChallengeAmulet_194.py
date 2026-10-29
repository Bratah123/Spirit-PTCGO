from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import island_challenge_amulet_passive

card = PokemonToolCardDef(
    guid="dcddc8d0-1d8d-54b0-8560-28cdd0d6c8ce",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandChallengeAmulet.Name",
    display_name="Island Challenge Amulet",
    searchable_by=["Island Challenge Amulet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=194,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    passive=island_challenge_amulet_passive,
)
