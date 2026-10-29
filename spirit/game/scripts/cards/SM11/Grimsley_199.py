from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import grimsley, grimsley_condition

card = SupporterCardDef(guid='5d564d00-7915-550f-870e-394143551841', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.Grimsley.Name', display_name='Grimsley', searchable_by=['Grimsley', 'Supporter'], subtypes=['Supporter'], collector_number=199, set_code='SM11', rarity=Rarities.Uncommon, effect=grimsley, condition=grimsley_condition)
