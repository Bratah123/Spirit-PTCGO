from spirit.game.card_effects.trainers import BigParasolPassive
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    passive=BigParasolPassive(),
    guid="62922a2d-57fd-5c5a-bbd0-9e89f435abd0",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BigParasol.Name",
    display_name="Big Parasol",
    searchable_by=["Big Parasol", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=199,
    set_code="SWSH3",
    rarity=Rarities.RareSecret
)
