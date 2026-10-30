"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(guid='161b8aa1-9094-596a-aec1-ea9e471eef9f', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name', display_name='Anorith', searchable_by=['Anorith', 'Stage 1', 'Anorith'], subtypes=['Stage 1'], collector_number=46, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.ClawFossil.Name', family_id=347, abilities=[Attack(title='Guard Claw', game_text="During your opponent's next turn, any damage done to Anorith by attacks is reduced by 20 (after applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=protect_next_turn(reduce=20)), Attack(title='X-Scissor', game_text='Flip a coin. If heads, this attack does 30 damage plus 20 more damage.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=flip_bonus(20))])
