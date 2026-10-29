from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import hapu, hapu_condition

card = SupporterCardDef(guid='b4863af3-49c5-51d7-af22-66305e1bba37', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.Hapu.Name', display_name='Hapu', searchable_by=['Hapu', 'Supporter'], subtypes=['Supporter'], collector_number=200, set_code='SM11', rarity=Rarities.Uncommon, effect=hapu, condition=hapu_condition)
