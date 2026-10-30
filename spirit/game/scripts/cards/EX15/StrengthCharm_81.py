"""StrengthCharm_74 wired."""
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import StrengthCharmPassive

card = PokemonToolCardDef(
    guid="60bb2ef7-569c-5a4e-9a75-4c15b17ddcd4",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=81,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    passive=StrengthCharmPassive()
)
