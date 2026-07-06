from spirit.game.card_effects.trainers import BigParasolPassive
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    passive=BigParasolPassive(),
    guid="fe4d1c10-cbc1-56ea-be68-613538aa27f0",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BigParasol.Name",
    display_name="Big Parasol",
    searchable_by=["Big Parasol", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=157,
    set_code="SWSH3",
    rarity=Rarities.Uncommon
)
