from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import island_challenge_amulet_passive

card = PokemonToolCardDef(
    guid="897323f4-ce91-5810-92a6-fb3a9af0a44b",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandChallengeAmulet.Name",
    display_name="Island Challenge Amulet",
    searchable_by=["Island Challenge Amulet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=265,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    passive=island_challenge_amulet_passive,
)
