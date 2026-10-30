"""StrengthCharm_74 wired."""
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import StrengthCharmPassive

card = PokemonToolCardDef(
    guid="619ee238-ff8b-5be5-870c-4f5d9312ff6a",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=StrengthCharmPassive()
)
