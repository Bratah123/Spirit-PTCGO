from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import multiply

card = PokemonCardDef(guid='4ed4bf35-aa40-593f-aadb-3270031625f5', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name', display_name='Sewaddle', searchable_by=['Sewaddle', 'Basic', 'Sewaddle'], subtypes=['Basic'], collector_number=6, set_code='SM11', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=540, abilities=[Attack(title='Multiply', game_text='Search your deck for up to 2 Sewaddle and put them onto your Bench. Then, shuffle your deck.', cost={PokemonTypes.COLORLESS: 1}, effect=multiply), Attack(title='Gnaw', cost={PokemonTypes.COLORLESS: 1}, damage=10)])
