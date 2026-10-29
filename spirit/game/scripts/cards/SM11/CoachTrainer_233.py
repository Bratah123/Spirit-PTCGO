from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import coach_trainer

card = SupporterCardDef(guid='14d502f5-c4be-50ca-b46e-90648b7d90b7', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.CoachTrainer.Name', display_name='Coach Trainer', searchable_by=['Coach Trainer', 'Supporter'], subtypes=['Supporter'], collector_number=233, set_code='SM11', rarity=Rarities.RareUltra, effect=coach_trainer)
