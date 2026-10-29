from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import EscapeBoardPassive

card = PokemonToolCardDef(
    guid="da3fdfc3-309e-510a-8661-55db132b1fed",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeBoard.Name",
    display_name="Escape Board",
    searchable_by=["Escape Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=167,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    passive=EscapeBoardPassive(),
)
