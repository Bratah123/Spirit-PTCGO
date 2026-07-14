from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import hp_bonus_tool

card = PokemonToolCardDef(
    guid="6cf61098-a412-5aa1-be7f-8eccb52f00b1",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BigCharm.Name",
    display_name="Big Charm",
    searchable_by=["Big Charm", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=158,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    passive=hp_bonus_tool(30)
)
