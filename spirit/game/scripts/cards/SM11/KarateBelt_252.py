from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import karate_belt_passive

card = PokemonToolCardDef(guid='a448d0e7-3b82-561a-be94-a375a343e4dc', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.KarateBelt.Name', display_name='Karate Belt', searchable_by=['Karate Belt', 'Pokémon Tool'], subtypes=['Pokémon Tool'], collector_number=252, set_code='SM11', rarity=Rarities.RareSecret, passive=karate_belt_passive)
