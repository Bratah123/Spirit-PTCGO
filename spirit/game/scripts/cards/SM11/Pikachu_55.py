from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import meal_time

card = PokemonCardDef(guid='7e28ea58-5166-5210-a803-be9dc8231ff6', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name', display_name='Pikachu', searchable_by=['Pikachu', 'Basic', 'Pikachu'], subtypes=['Basic'], collector_number=55, set_code='SM11', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=25, abilities=[Attack(title='Meal Time', game_text='Flip a coin until you get tails. For each heads, draw a card.', cost={PokemonTypes.LIGHTNING: 1}, effect=meal_time), Attack(title='Gnaw', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=20)])
