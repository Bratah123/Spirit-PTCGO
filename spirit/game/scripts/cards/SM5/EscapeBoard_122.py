from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import EscapeBoardPassive

card = PokemonToolCardDef(
    guid="fc22b6a2-1070-5011-be88-374afbfae4bc",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeBoard.Name",
    display_name="Escape Board",
    searchable_by=["Escape Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=122,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    passive=EscapeBoardPassive(),
)
