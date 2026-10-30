"""StrengthCharm_74 wired."""
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import StrengthCharmPassive

card = PokemonToolCardDef(
    guid="656950fa-b639-5bb2-9557-215aed817e77",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=74,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    passive=StrengthCharmPassive()
)
