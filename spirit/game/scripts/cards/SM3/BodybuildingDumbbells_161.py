from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import hp_bonus_tool
from spirit.game.card_effects.sm3 import is_stage1

card = PokemonToolCardDef(
    guid="8f065d6b-55c4-5e65-b3a2-e52cc29ebf22",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BodybuildingDumbbells.Name",
    display_name="Bodybuilding Dumbbells",
    searchable_by=["Bodybuilding Dumbbells", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=161,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    passive=hp_bonus_tool(40, holder_pred=is_stage1),)
