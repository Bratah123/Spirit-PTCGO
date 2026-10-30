from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import BalloonBerryPassive

card = PokemonToolCardDef(
    guid="9127027c-8219-5bfa-b861-203464b0e059",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BalloonBerry.Name",
    display_name="Balloon Berry",
    searchable_by=["Balloon Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=84,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=BalloonBerryPassive(),
)
