"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='6c2f13ff-0746-5fb4-85a1-1420d3d4abfd', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name', display_name='Pikachu', searchable_by=['Pikachu', 'Basic', 'Pikachu'], subtypes=['Basic'], collector_number=70, set_code='DP5', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=25, abilities=[Attack(title='Quick Attack', game_text='Flip a coin. If heads, this attack does 10 damage plus 10 more damage.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=flip_bonus(10)), Attack(title='Volt Tackle', game_text='Pikachu does 10 damage to itself.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=recoil_attack(10, damage=50))])
