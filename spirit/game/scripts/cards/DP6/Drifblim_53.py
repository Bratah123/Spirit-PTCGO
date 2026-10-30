"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(guid='ded8f3fb-d1ae-5d4d-a86d-afee9e42bb72', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name', display_name='Drifblim', searchable_by=['Drifblim', 'Stage 1', 'Drifblim'], subtypes=['Stage 1'], collector_number=53, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name', family_id=425, abilities=[Attack(title='Expand', game_text="During your opponent's next turn, any damage done to Drifblim by attacks is reduced by 10 (after applying Weakness and Resistance).", cost={PokemonTypes.PSYCHIC: 1}, damage=30, effect=protect_next_turn(reduce=10)), Attack(title='Whirlwind', game_text='Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.', cost={PokemonTypes.COLORLESS: 3}, damage=60, effect=gust_attack(opponent_chooses=True))])
