from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import nature_wave_cost_passive

card = PokemonCardDef(guid='c979c589-a1d7-546e-9e74-80a7ee3a5f5a', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.TapuFini.Name', display_name='Tapu Fini', searchable_by=['Tapu Fini', 'Basic', 'TapuFini'], subtypes=['Basic'], collector_number=53, set_code='SM11', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, family_id=788, abilities=[Attack(title='Razor Fin', cost={PokemonTypes.WATER: 1}, damage=20), Attack(title='Nature Wave', game_text='If your opponent has any Ultra Beasts in play, this attack can be used for Colorless.', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=100)], passive=nature_wave_cost_passive)
