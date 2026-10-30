"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='7681326c-34d1-54bc-97d0-5b50de43b2c0', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name', display_name='Voltorb', searchable_by=['Voltorb', 'Basic', 'Voltorb'], subtypes=['Basic'], collector_number=117, set_code='DP3', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=100, abilities=[Attack(title='Speed Ball', cost={PokemonTypes.LIGHTNING: 1}, damage=20), Attack(title='Big Explosion', game_text='Voltorb does 50 damage to itself.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=50, effect=recoil_attack(50, damage=50))])
