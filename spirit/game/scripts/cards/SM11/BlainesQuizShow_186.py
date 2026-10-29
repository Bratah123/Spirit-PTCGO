from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import blaines_quiz_show, blaines_quiz_show_condition

card = SupporterCardDef(guid='a8f982cb-3831-5788-97f0-2abb7064c632', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuizShow.Name', display_name="Blaine's Quiz Show", searchable_by=["Blaine's Quiz Show", 'Supporter'], subtypes=['Supporter'], collector_number=186, set_code='SM11', rarity=Rarities.Uncommon, effect=blaines_quiz_show, condition=blaines_quiz_show_condition)
