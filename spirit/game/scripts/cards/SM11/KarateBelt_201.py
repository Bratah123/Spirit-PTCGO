from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import karate_belt_passive

card = PokemonToolCardDef(guid='06cf15ae-a698-5e9a-aca6-5cbeda20e770', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.KarateBelt.Name', display_name='Karate Belt', searchable_by=['Karate Belt', 'Pokémon Tool'], subtypes=['Pokémon Tool'], collector_number=201, set_code='SM11', rarity=Rarities.Uncommon, passive=karate_belt_passive)
