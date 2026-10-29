from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import EscapeBoardPassive

card = PokemonToolCardDef(
    guid="4b14e000-3a65-5555-8cb4-3dd6cafde104",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeBoard.Name",
    display_name="Escape Board",
    searchable_by=["Escape Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=175,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    passive=EscapeBoardPassive(),
)
