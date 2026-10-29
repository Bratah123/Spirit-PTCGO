from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import coach_trainer

card = SupporterCardDef(guid='0697d68b-a1f8-5182-bc75-290b5d6428f6', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.CoachTrainer.Name', display_name='Coach Trainer', searchable_by=['Coach Trainer', 'Supporter'], subtypes=['Supporter'], collector_number=192, set_code='SM11', rarity=Rarities.Uncommon, effect=coach_trainer)
