from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import grimsley, grimsley_condition

card = SupporterCardDef(guid='ce0ad422-0c2b-5809-b9ef-7dcbaa198c04', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.Grimsley.Name', display_name='Grimsley', searchable_by=['Grimsley', 'Supporter'], subtypes=['Supporter'], collector_number=234, set_code='SM11', rarity=Rarities.RareUltra, effect=grimsley, condition=grimsley_condition)
