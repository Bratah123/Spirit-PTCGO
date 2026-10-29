from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import poke_maniac

card = SupporterCardDef(guid='34c81731-196f-51d0-b671-e79bf01a74b0', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.PokeManiac.Name', display_name='Poké Maniac', searchable_by=['Poké Maniac', 'Supporter'], subtypes=['Supporter'], collector_number=204, set_code='SM11', rarity=Rarities.Uncommon, effect=poke_maniac)
