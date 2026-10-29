from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm11 import weakness_guard_passive

card = EnergyCardDef(guid='1a405954-c087-5c16-b5c4-2a7f45b546df', key='SM11', name='Weakness Guard Energy', display_name='Weakness Guard Energy', searchable_by=['Weakness Guard Energy', 'Special'], subtypes=['Special'], collector_number=258, set_code='SM11', rarity=Rarities.RareSecret, energy_type=PokemonTypes.COLORLESS, is_special=True, passive=weakness_guard_passive)
